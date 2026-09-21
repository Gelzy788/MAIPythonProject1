import argparse

import sys

from toolkit.calculator import calc_manager
from toolkit.errors import CalculatorError

def main():
    parser = argparse.ArgumentParser(prog="toolkit")
    subparser = parser.add_subparsers(dest="command", required=True)

    sub_calc = subparser.add_parser("calc", help='Калькулятор: \tcalc "EXPRESSION"')
    sub_calc.add_argument("example", help="Математическое выражение")

    sub_convert = subparser.add_parser("convert", help="Конвертер: \tconvert VALUE --from UNIT --to UNIT")
    sub_convert.add_argument("value", type=float)
    sub_convert.add_argument("--from", dest="from_unit", required=True)
    sub_convert.add_argument("--to", dest="to_unit", required=True)

    args = parser.parse_args()

    if args.command == "calc":
        try:
            print(calc_manager(args.example))
        except CalculatorError as err:
            print(str(err), file=sys.stderr)
            sys.exit(2)
    elif args.command == "convert":
        print("convert:")
        print("value:", args.value)
        print(f"from {args.from_unit} to {args.to_unit}")

if __name__ == "__main__":
    main()