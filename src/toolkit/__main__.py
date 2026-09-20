import argparse

def main():
    parser = argparse.ArgumentParser(prog="toolkit")
    subparser = parser.add_subparsers(dest="command", required=True)

    sub_calc = subparser.add_parser("calc", help="Калькулятор")
    sub_calc.add_argument("example")

    sub_convert = subparser.add_parser("convert", help="Конвертация")
    sub_convert.add_argument("convert") # TODO: Сделать структуру ввода команды как в ТЗ

    args = parser.parse_args()

    if args.command == "calc":
        print("hello")
    elif args.command == "convert":
        print("convert")

if __name__ == "__main__":
    main()