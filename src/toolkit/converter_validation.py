from toolkit.units import UNIT_GROUPS
from toolkit.errors import (InvalidUnitError,
                            InvalidValueError,
                            IncompatibleUnitsError)

def get_group(unit: str) -> str:
    if unit in ["c", "f", "k"]:
        return "temperature"
    elif unit[-1] == "m":
        return "length"
    elif unit[-1] == "g":
        return "mass"
    else:
        raise InvalidUnitError(unit)

def validate_converter(value, unit1, unit2):
    check_unknown_units(unit1, unit2)
    check_incompetible_units(unit1, unit2)
    check_value(value)

def check_unknown_units(unit1: str, unit2: str):
    if unit1 not in UNIT_GROUPS.keys():
        raise InvalidUnitError(unit1)
    if unit2 not in UNIT_GROUPS.keys():
        raise InvalidUnitError(unit2)

def check_incompetible_units(unit1: str, unit2: str):
    if UNIT_GROUPS[unit1] != UNIT_GROUPS[unit2]:
        raise IncompatibleUnitsError(unit1, unit2)

def check_value(value: str):
    try: float(value)
    except ValueError:
        raise InvalidValueError(value)