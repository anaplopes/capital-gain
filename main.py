import sys
from enum import Enum
from typing import List
from dataclasses import dataclass


class Operation(str, Enum):
    BUY = "buy"
    SELL = "sell"


@dataclass
class In:
    operation: Operation
    unit_cost: float
    quantity: int


@dataclass
class Out:
    tax: float


def tax_percentage(operations: List[In]) -> List[Out]:
    """Função responsável por calcular o percentual de imposto pago
    sobre o lucro obtido em operações de venda.

    Args:
        operations (List[In]): operações de compra e venda

    Returns:
        List[Out]: percentual de imposto pago nas operações
    """
    out = []
    prejuizo = 0
    for op in operations:
        if op.operation == "buy":
            out.append({"tax":0.00})
        else:
            price_sell = op.unit_cost * op.quantity
            if price_sell <= 20000:
                out.append({"tax":0.00})
            else:
                ...

    return out




# ENTRADA
# [{"operation":"buy", "unit_cost":10.00, "quantity": 10000}, {"operation":"sell", "unit_cost":20.00, "quantity": 5000}]
# [{"operation":"buy", "unit_cost":20.00, "quantity": 10000}, {"operation":"sell", "unit_cost":10.00, "quantity": 5000}]


# SAIDA
# [{"tax":0.00}, {"tax":10000.00}]
# [{"tax":0.00}, {"tax":0.00}]



for line in sys.stdin:
    if "" == line.rstrip():
        break

    result = tax_percentage(operations=line)
    sys.stdout.write(result)
