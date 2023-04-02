from typing import List, Tuple
from .schemas import Input


class StockMarket:
    def calculate_weighted_average(
        self,
        weighted_average: float,
        qtd_stocks: int,
        quantity: int,
        unit_cost: float
    ) -> float:
        """Calcula a preço médio ponderado de compra.

        Args:
            weighted_average (float): Preço médio ponderado atual
            qtd_stocks (int): Quantidade de ações atual
            quantity (int): Quantidade de ações compradas
            unit_cost (float): Preço unitário da ação comprada

        Returns:
            float: Novo preço médio ponderado
        """

        current_inventory = qtd_stocks * weighted_average
        total_cost_operation = unit_cost * quantity
        sum_stocks = qtd_stocks + quantity
        sum_inventory = current_inventory + total_cost_operation
        return sum_inventory / sum_stocks

    def result_statement(
        self, quantity: int, unit_cost: float, weighted_average: float
    ) -> Tuple[float, float]:
        """Faz a declaração de resultado da operação.

        Args:
            quantity (int): Quantidade de ações vendidas
            unit_cost (float): Preço unitário da ação vendida
            weighted_average (float): Preço médio ponderado de compra

        Returns:
            Tuple[float, float]: Resultado e custo da operação
        """

        result_operation = unit_cost - weighted_average
        operation_cost = result_operation * quantity
        return result_operation, operation_cost

    def purchase_tax(self) -> float:
        """Calcula o imposto sobre a compra de ações.

        Returns:
            dict: Imposto pago para operação de compra
        """

        return 0.00

    def sales_tax(
        self,
        quantity: int,
        unit_cost: float,
        result_operation: float,
        total_result_operations: float,
    ) -> float:
        """Calcula o imposto sobre a venda de ações.

        Args:
            quantity (int): Quantidade de ações vendidas
            unit_cost (float): Preço unitário da ação vendida
            result_operation (float): Resultado da operação
            (+) lucro | (-) prejuizo
            total_result_operations (float): Total do resultado das operações
        Returns:
            dict: Imposto pago para operação de venda
        """

        total_cost_operation = unit_cost * quantity
        if result_operation > 0 and total_cost_operation <= 20000:
            return 0.00

        aliquot = 20 / 100
        tax = (
            round(total_result_operations * aliquot, 2)
            if total_result_operations > 0
            else 0.00
        )
        return tax

    def calculate_taxs(self, operations: List[Input]) -> List[dict]:
        """Calcula o imposto a ser pago sobre lucros ou prejuízos de operações
        no mercado financeiro de ações.

        Args:
            operations (List[dict]): Lista de operações do mercado
        financeiro de ações

        Returns:
            List[dict]: Lista contendo o imposto pago para cada
        operação recebida
        """

        qtd_stocks: int = 0
        weighted_average: float = 0
        total_result_operations: float = 0

        for op in operations:
            if op.operation == "buy":
                weighted_average = self.calculate_weighted_average(
                    weighted_average=weighted_average,
                    qtd_stocks=qtd_stocks,
                    quantity=op.quantity,
                    unit_cost=op.unit_cost,
                )
                op.tax = self.purchase_tax()
                qtd_stocks += op.quantity

            if op.operation == "sell":
                result_operation, operation_cost = self.result_statement(
                    quantity=op.quantity,
                    unit_cost=op.unit_cost,
                    weighted_average=weighted_average,
                )
                total_result_operations += operation_cost
                op.tax = self.sales_tax(
                        quantity=op.quantity,
                        unit_cost=op.unit_cost,
                        result_operation=result_operation,
                        total_result_operations=total_result_operations,
                    )
                qtd_stocks -= op.quantity
                total_result_operations = total_result_operations \
                    if total_result_operations < 0 else 0

        return [{"tax": op.tax} for op in operations]
