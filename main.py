import sys
import json
from typing import List


def tax_percentage(operations: List[dict]) -> List[dict]:
    qtd_shares = 0
    current_weighted_average = 0
    amount_op_result = 0

    for op in operations:

        if op["operation"] == "buy":
            op.update({"tax": 0.00})
            stock = qtd_shares * current_weighted_average
            price_purchase = op["quantity"] * op["unit-cost"]
            current_weighted_average = (stock + price_purchase) / (qtd_shares + op["quantity"])
            qtd_shares += op["quantity"]

        if op["operation"] == "sell":
            op_result = op["unit-cost"] - current_weighted_average
            price_sell = op["unit-cost"] * op["quantity"]
            if op_result > 0 and price_sell <= 20000:
                op.update({"tax": 0.00})
                qtd_shares -= op["quantity"]

            else:
                amount_op_result += (op_result * op["quantity"])
                tax = round(amount_op_result * (20 / 100), 2) if amount_op_result > 0 else 0.00
                op.update({"tax": tax})
                qtd_shares -= op["quantity"]
                amount_op_result = 0 if amount_op_result > 0 else amount_op_result

    return operations


for line in sys.stdin:
    if "" == line.rstrip():
        break

    operations = json.loads(line)
    tax = tax_percentage(operations=operations)
    print(json.dumps(tax) + '\n')
    # sys.stdout.write(json.dumps(tax) + '\n\n')
    # sys.stdout.flush()
sys.exit('Finished...')
