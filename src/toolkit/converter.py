from toolkit.constants import UNIT_GROUPS, UNITS
from toolkit.converter_validation import validate_converter
from toolkit.errors import TemperatureBelowAbsZero


def converter_manager(value: str, from_unit: str, to_unit: str) -> float:
    """Главная входная точка всей программы-конвертера
    Является центром конвертера, вызывает все функции

    Args:
        value: Число, которое нужно перевест
        from_unit: Из какой величины перевести
        to_unit: В какую величину перевести

    Returns:
        Результат конвертации
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    validate_converter(value, from_unit, to_unit)
    return convert(float(value), from_unit, to_unit)

def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Конвертация температуры

    Args:
        value: Число, которое нужно перевест
        from_unit: Из какой величины перевести
        to_unit: В какую величину перевести

    Returns:
        Результат конвертации температуры
    """
    # получаем коэффициенты перевода температур
    from_unit_data = UNITS["temperature"][from_unit]
    to_unit_data = UNITS["temperature"][to_unit]
    
    value_in_kelvin = (value - from_unit_data["zero_offset"]) / from_unit_data["coef"]
    result_value = value_in_kelvin * to_unit_data["coef"] + to_unit_data["zero_offset"]
    
    return result_value

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Конвертер
        Конвертирует величины и выдает результат

    Args:
        value: Число, которое нужно перевест
        from_unit: Из какой величины перевести
        to_unit: В какую величину перевести

    Raises:
        TemperatureBelowAbsZero: Если на вход подана температура ниже абсолютного нуля

    Returns:
        Результат перевода
    """
    
    group = UNIT_GROUPS[from_unit]
    
    if group == "temperature":
        if value < UNITS["temperature"][from_unit]["zero_offset"]:
            raise TemperatureBelowAbsZero
        else:
            return convert_temperature(value, from_unit, to_unit)
    else:
        coef = UNITS[group][from_unit] / UNITS[group][to_unit]
        return value / coef
