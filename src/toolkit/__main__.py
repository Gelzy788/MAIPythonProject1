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

    Считывает аргументы командной строки и возвращает их.

    Args:
        argv: Список аргументов. Если None, берётся sys.argv.

    Returns:
        Разобранные аргументы (argparse.Namespace)
    """
    formatter = argparse.RawDescriptionHelpFormatter

    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="Консольный калькулятор и конвертер величин.",
        epilog=(
            "примеры:\n"
            '  python -m toolkit calc "2 + 3 * 4"\n'
            "  python -m toolkit convert 1.5 --from km --to m\n"
            "\n"
            "подробнее о команде: python -m toolkit КОМАНДА --help"
        ),
        formatter_class=formatter,
    )
    subparser = parser.add_subparsers(
        dest="command", required=True, title="команды", metavar="КОМАНДА"
    )

    # Команда calc
    sub_calc = subparser.add_parser(
        "calc",
        help="вычислить математическое выражение",
        description="Вычисляет математическое выражение и выводит результат.",
        epilog=(
            "операции:\n"
            "  +  -  *  /    сложение, вычитание, умножение, деление\n"
            "  //  %         целочисленное деление и остаток (только целые числа)\n"
            "  ( )           скобки для изменения порядка действий\n"
            "  -5  +5        унарные минус и плюс\n"
            "\n"
            "дробная часть отделяется точкой: 2.5, а не 2,5\n"
            "числа с точкой (даже 10.0) считаются дробными: 10.0 // 3 — ошибка\n"
            "\n"
            "примеры:\n"
            '  python -m toolkit calc "2 + 3 * 4"      → 14\n'
            '  python -m toolkit calc "(2 + 3) * 4"    → 20\n'
            '  python -m toolkit calc "7 // 2"         → 3\n'
            '  python -m toolkit calc -- "-5 + 3"      → -2\n'
            "\n"
            "выражение берите в кавычки. если оно начинается с минуса,\n"
            "поставьте перед ним --, иначе оно будет принято за флаг"
        ),
        formatter_class=formatter,
    )
    sub_calc.add_argument(
        "example", metavar="ВЫРАЖЕНИЕ", help='математическое выражение, например "2 + 2"'
    )

    # Команда convert
    sub_convert = subparser.add_parser(
        "convert",
        help="перевести значение из одной единицы в другую",
        description="Переводит значение из одной единицы измерения в другую.",
        epilog=(
            "единицы (регистр не важен):\n"
            "  длина:        mm, cm, m, km\n"
            "  масса:        g, kg\n"
            "  температура:  c (Цельсий), f (Фаренгейт), k (Кельвин)\n"
            "\n"
            "переводить можно только внутри одной группы: km → kg — ошибка\n"
            "\n"
            "примеры:\n"
            "  python -m toolkit convert 1.5 --from km --to m     → 1500\n"
            "  python -m toolkit convert 2500 --from g --to kg    → 2.5\n"
            "  python -m toolkit convert -40 --from c --to f      → -40"
        ),
        formatter_class=formatter,
    )
    sub_convert.add_argument("value", metavar="ЗНАЧЕНИЕ", help="число для перевода, например 1.5")
    sub_convert.add_argument(
        "--from", dest="from_unit", required=True, metavar="ЕДИНИЦА", help="исходная единица"
    )
    sub_convert.add_argument(
        "--to", dest="to_unit", required=True, metavar="ЕДИНИЦА", help="целевая единица"
    )

    return parser.parse_args(argv)


def start_calculator(example: str):
    """Запуск калькулятора

    Запускает калькулятор, сохраняет в историю успешные вычисления.

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
        # Форматирование результата для более точного вывода
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

    Единая точка входа программы. Запускает калькулятор или конвертер
    в зависимости от введённой команды.

    Args:
        argv: Список аргументов. Если None, берётся sys.argv.
    """
    args = parse_args(argv)  # Данные всех аргументов, введенных пользователем

    if args.command == "calc":
        start_calculator(args.example)

    elif args.command == "convert":
        start_converter(args.value, args.from_unit, args.to_unit)


if __name__ == "__main__":
    main()
