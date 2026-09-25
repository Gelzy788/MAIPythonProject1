import argparse
import sys
from decimal import Decimal

from toolkit.calculator import calc_manager
from toolkit.converter import converter_manager
from toolkit.errors import CalculatorError, ConverterError
from toolkit.history_saver import (
    add_calculation_to_history,
    add_convertation_to_history,
)


def main():
    # Создание парсера и субпарсера
    parser = argparse.ArgumentParser(prog="toolkit")
    subparser = parser.add_subparsers(dest="command", required=True)

    # Инициализация аргументов для calc
    sub_calc = subparser.add_parser("calc", help='Калькулятор: \tcalc "EXPRESSION"')
    sub_calc.add_argument("example", help="Математическое выражение")

    # Инициализация элементов для converter
    sub_convert = subparser.add_parser("convert", help="Конвертер: \tconvert VALUE --from UNIT --to UNIT")
    sub_convert.add_argument("value")
    sub_convert.add_argument("--from", dest="from_unit", required=True)
    sub_convert.add_argument("--to", dest="to_unit", required=True)

    args = parser.parse_args() # Данные всех аргументов, введенных пользователем

    if args.command == "calc":
        try:
            # Получение результата
            result = calc_manager(args.example)
            print(result)
        except CalculatorError as err:
            print(str(err), file=sys.stderr)
            sys.exit(2)
        
        # Загрузка вычисления в историю
        try:
            add_calculation_to_history(args.example, result)
        except OSError:
            print("Сохранить историю вычислений не поулчилось!")
        
    elif args.command == "convert":
        try:
            # Конвертация величин
            converted_value = converter_manager(args.value, args.from_unit, args.to_unit)
            # Форматирвоания результата для более точного вывода
            rounded_result = Decimal(f"{converted_value:.12g}")
            result = format(rounded_result.normalize(), "f")
            # Сохранение перконвертации в историю
            add_convertation_to_history(args.value, args.from_unit, args.to_unit, result)
            
            print(result)
        except ConverterError as err:
            print(str(err), file=sys.stderr)
            sys.exit(2)

if __name__ == "__main__":
    main()