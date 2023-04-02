import sys
import json
from .schemas import Input
from .stock_market import StockMarket
from json.decoder import JSONDecodeError
from pydantic.error_wrappers import ValidationError


def main():
    for line in sys.stdin:
        if "" == line.rstrip():
            break

        try:
            operations = json.loads(line)
            for idx, element in enumerate(operations):
                element = {k.replace("-", "_"): v for k, v in element.items()}
                element = Input(**element)
                operations[idx] = element
        except JSONDecodeError as e:
            sys.stdout.write(f"JSONDecodeError: {e}\n")
        except ValidationError as e:
            sys.stdout.write(f"ValidationError: {e}\n")
        else:
            taxs = StockMarket().calculate_taxs(operations=operations)
            sys.stdout.write(json.dumps(taxs) + "\n")
            sys.stdout.flush()

    sys.exit("Finished!")


if __name__ == "__main__":
    main()
