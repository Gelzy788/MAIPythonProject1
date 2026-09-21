import argparse

import sys

from toolkit.calculator import calc_manager
from toolkit.errors import CalculatorError

def main():
    parser = argparse.ArgumentParser(prog="toolkit")
    subparser = parser.add_subparsers(dest="command", required=True)

    sub_calc = subparser.add_parser("calc", help="Калькулятор")
    sub_calc.add_argument("example")

    sub_convert = subparser.add_parser("convert", help="Конвертация")
    sub_convert.add_argument("convert") # TODO: Сделать структуру ввода команды как в ТЗ

    args = parser.parse_args()

    if args.command == "calc":
        try:
            print(calc_manager(args.example))
        except CalculatorError as err:
            print(str(err), file = sys.stderr)
            sys.exit(2)
    elif args.command == "convert":
        print("convert")

if __name__ == "__main__":
    main()