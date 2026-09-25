from toolkit.constants import UNIT_GROUPS
from toolkit.errors import (InvalidUnitError,
                            InvalidValueError,
                            IncompetibleUnitsError)

from math import isnan

def validate_converter(value, unit1: str, unit2: str):
    """Менеджер валидации конвертера
    
        Вызывает все функции, связанные с валидацией конвертера
            и является единой точкой входа на данный этап
        
        Args:
            tokenized_example: Токенизированное выражение в формате спика
    """
    check_unknown_unit(unit1)
    check_unknown_unit(unit2)
    check_incompetible_units(unit1, unit2)
    check_value(value)

def check_unknown_unit(unit: str):
    """Валидирует неизвестные величины
        
        Функция проверяет, известна ли данная ей величина программе
        Если нет - вызывает ошибку

    Args:
        unit: Величина

    Raises:
        InvalidUnitError: Если величина неизвестна
    """
    if unit not in UNIT_GROUPS:
        raise InvalidUnitError(unit)

def check_incompetible_units(unit1: str, unit2: str):
    """Проверяет, принадлежат ли величины одной группе
        
        Проверяет, принадлежит ли две, поданных на вход величины, одной группе,
        то есть можно ли их переводить друг между другом

    Args:
        unit1: Величина 1
        unit2: Величина 2

    Raises:
        IncompetibleUnitsError: Если величины принадлежат разным группам
    """
    if UNIT_GROUPS[unit1] != UNIT_GROUPS[unit2]:
        raise IncompetibleUnitsError(unit1, unit2)

def check_value(value: str):
    """Проверяет правильность написания числа, когда оно еще в str
        
    Args:
        value: Число в формате строки

    Raises:
        InvalidValueError: Если число написано неправильно или является NaN
    """
    try:
        float_value = float(value)
        if isnan(float_value):
            raise InvalidValueError(value)
    except ValueError:
        raise InvalidValueError(value)
