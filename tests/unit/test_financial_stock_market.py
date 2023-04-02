import unittest
from taxcli.schemas import Input
from taxcli.stock_market import StockMarket


class TestsFinancialStockMarket(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.fsm = StockMarket()
        self.buy = Input(
            **{"operation": "buy", "unit_cost": 10.00, "quantity": 10000})
        self.sell = Input(
            **{"operation": "sell", "unit_cost": 20.00, "quantity": 5000})

    def test_calculate_weighted_average(self):
        _func = self.fsm.calculate_weighted_average(
            weighted_average=0,
            qtd_stocks=0,
            quantity=self.buy.quantity,
            unit_cost=self.buy.unit_cost,
        )
        _output = 10.00
        self.assertEqual(_output, _func)
        self.assertIsInstance(_func, float)

    def test_result_statement(self):
        _func = self.fsm.result_statement(
            quantity=self.sell.quantity,
            unit_cost=self.sell.unit_cost,
            weighted_average=10.00,
        )
        _output = (10.00, 50000.00)
        self.assertEqual(_output, _func)
        self.assertIsInstance(_func, tuple)

    def test_purchase_tax(self):
        _func = self.fsm.purchase_tax()
        _output = 0.00
        self.assertEqual(_output, _func)
        self.assertIsInstance(_func, float)

    def test_sales_tax(self):
        _func = self.fsm.sales_tax(
            quantity=self.sell.quantity,
            unit_cost=self.sell.unit_cost,
            result_operation=10.00,
            total_result_operations=50000.00,
        )
        _output = 10000.00
        self.assertEqual(_output, _func)
        self.assertIsInstance(_func, float)

    def test_calculate_taxs(self):
        operations = []
        operations.append(self.buy)
        operations.append(self.sell)
        _func = self.fsm.calculate_taxs(operations=operations)
        _output = [{"tax": 0.00}, {"tax": 10000.00}]
        self.assertEqual(_output, _func)
        self.assertIsInstance(_func, list)


if __name__ == "__name__":
    unittest.main()
