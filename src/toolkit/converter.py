from decimal import Decimal

from toolkit.validation import validate_converter
from toolkit.errors import InvalidUnitError

UNITS = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": 0.001,
    "g": 1,
    "kg": 0.001
}

def converter_manager(value: float, from_unit: str, to_unit: str) -> float:
    validate_converter()
    
    if get_group(from_unit) in ["length", "mass"]:
        return convert_len_and_weight(value, from_unit, to_unit)
    else:
        return convert_temperature(value, from_unit, to_unit)
    
def get_group(unit: str) -> str:
    if unit in ["c", "f", "k"]:
        return "temperature"
    elif unit in UNITS:
        if unit[-1] == "m":
            return "length"
        elif unit[-1] == "g":
            return "mass"
    else:
        raise InvalidUnitError(unit)
    
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    pass

def convert_len_and_weight(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
        
    coef = UNITS[from_unit]
    coef /= UNITS[to_unit]
        
    return value / coef

if __name__ == "__main__":
    print(convert_len_and_weight(35, "Km", "m"))