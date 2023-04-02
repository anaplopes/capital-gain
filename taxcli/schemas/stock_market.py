from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Operation(str, Enum):
    BUY = "buy"
    SELL = "sell"


class Input(BaseModel):
    operation: str
    unit_cost: float
    quantity: int
    tax: Optional[float] = 0.00
