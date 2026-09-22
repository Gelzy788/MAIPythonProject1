import argparse

from decimal import Decimal

import sys

from toolkit.calculator import calc_manager
from toolkit.converter import converter_manager
from toolkit.errors import CalculatorError, ConverterError

def main():
    parser = argparse.ArgumentParser(prog="toolkit")
    subparser = parser.add_subparsers(dest="command", required=True)

    sub_calc = subparser.add_parser("calc", help='Калькулятор: \tcalc "EXPRESSION"')
    sub_calc.add_argument("example", help="Математическое выражение")

    sub_convert = subparser.add_parser("convert", help="Конвертер: \tconvert VALUE --from UNIT --to UNIT")
    sub_convert.add_argument("value")
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
        try:
            converted_value = converter_manager(args.value, args.from_unit, args.to_unit)
            rounded_result = Decimal(f"{converted_value:.12g}")
            print(format(rounded_result.normalize(), "f"))
        except ConverterError as err:
            print(str(err), file=sys.stderr)
            sys.exit(2)

if __name__ == "__main__":
    main()