import sys
import json
from .financial_stock_market import FinancialStockMarket


def main():
    for line in sys.stdin:
        if "" == line.rstrip():
            break

        operations = json.loads(line)
        taxs = FinancialStockMarket().calculate_taxs(operations=operations)
        sys.stdout.write(json.dumps(taxs) + '\n')
        sys.stdout.flush()
    sys.exit('Finished!')


if __name__ == '__main__':
    main()
