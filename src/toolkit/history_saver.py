from json import load, JSONDecodeError, dump
from pathlib import Path
from toolkit.constants import HISTORY_FILENAME, HISTORY_PATH
from toolkit.errors import HistorySaveError


def add_calculation_to_history(example: str, result: float):
    """Добавление нового вычисления из калькулятора в json с историей

        Является входной точкой для сохранения истории калькулятора.
        Вызывает все нужные функции и руководит процессом

    Args:
        example: Выражение
        result: Результат вычисления
    """
    history_data = read_history_file()
    new_data = {"type": "calculation",
                "example": example,
                "result": result}
    history_data.append(new_data)
    save_file(history_data)

def add_convertation_to_history(value: str, from_unit: str, to_unit: str, result: str):
    """Добавление новой конвертации из конвертера в json с историей

    Является входной точкой для сохранения истории конвертера.
    Вызывает все нужные функции и руководит процессом

    Args:
        value: Число, которое нужно перевест
        from_unit: Из какой величины перевести
        to_unit: В какую величину перевести
        result: Результат конвертации
    """
    history_data = read_history_file()
    new_data = {"type": "convertation",
                "value": value,
                "from_unit": from_unit,
                "to_unit": to_unit,
                "result": result}
    history_data.append(new_data)
    save_file(history_data)

def read_history_file() -> list:
    """Читает файл истории
    
        Читает файл истории для будущего его дополнения

    Returns:
        Данные из json файла с историей операций
    """
    try:
        HISTORY_PATH.mkdir(exist_ok=True)
        with open(HISTORY_PATH / HISTORY_FILENAME, "r", encoding="utf-8") as file:
            data = load(file)
    except (JSONDecodeError, FileNotFoundError) as err:
        data = []
    return data

def save_file(data: list):
    """Сохраняет файл с изменениями
    
        Записывает в файл новые данные с новой операцией

    Args:
        data: Данные, что нужно записать в файл

    Raises:
        HistorySaveError: Если произошла ошибка взаимодействия с файлом
    """
    try:
        HISTORY_PATH.mkdir(exist_ok=True)
        with open(HISTORY_PATH / HISTORY_FILENAME, "w", encoding="utf-8") as file:
            dump(data, file, indent=4)
    except OSError:
        raise HistorySaveError()
