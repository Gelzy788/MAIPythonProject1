import argparse
import sys
from decimal import Decimal

from toolkit.calculator import calc_manager
from toolkit.converter import converter_manager
from toolkit.errors import CalcConverterError, HistorySaveError
from toolkit.history_saver import (
    add_calculation_to_history,
    add_convertation_to_history,
)


def parse_args(argv=None):
    """Парсер аргументов CLI
    
        Ссчитывает аргументы из CLI и возвращает их
        
        Returns:
            Аргументы из CLI
    """
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
    
    return parser.parse_args(argv)

def start_calculator(example: str):
    """ Запуск калькулятора

        Запускает калькулятор, сохраняет в историю успешные вычисления
    Args:
        example: Математическое выражение
    """
    try:
        # Получение результата
        result = calc_manager(example)
        print(result)
    except CalcConverterError as err:
        print(str(err), file=sys.stderr)
        sys.exit(2)
    
    # Загрузка вычисления в историю
    try:
        add_calculation_to_history(example, result)
    except HistorySaveError as err:
        print(str(err), file=sys.stderr)
        sys.exit(2)

def start_converter(value: str, from_unit: str, to_unit: str):
    """Запуск конвертера

    Args:
        value: Значение для конвертации
        from_unit: Из какой величины конвертировать
        to_unit: В какую величину конвертировать
    """
    try:
        # Конвертация величин
        converted_value = converter_manager(value, from_unit, to_unit)
        # Форматирвоания результата для более точного вывода
        rounded_result = Decimal(f"{converted_value:.12g}")
        result = format(rounded_result.normalize(), "f")
        
        print(result)
    except CalcConverterError as err:
        print(str(err), file=sys.stderr)
        sys.exit(2)
    
    # Загрузка конвертации в историю
    try:
        add_convertation_to_history(value, from_unit, to_unit, result)
    except HistorySaveError as err:
        print(str(err), file=sys.stderr)
        sys.exit(2)

def main(argv=None):
    """Главная функция
    
        Является единой точкой входа и выхода программы
        Запускае блоки программы в зависимости от запроса(calculator/converter)
    """

    args = parse_args(argv) # Данные всех аргументов, введенных пользователем
    
    if args.command == "calc":
        start_calculator(args.example)
        
    elif args.command == "convert":
        start_converter(args.value, args.from_unit, args.to_unit)

if __name__ == "__main__":
    main()