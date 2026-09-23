from toolkit.constants import UNIT_GROUPS
from toolkit.errors import (InvalidUnitError,
                            InvalidValueError,
                            IncompetibleUnitsError)

from math import isnan

def validate_converter(value, unit1: str, unit2: str):
    check_unknown_unit(unit1)
    check_unknown_unit(unit2)
    check_incompetible_units(unit1, unit2)
    check_value(value)

def check_unknown_unit(unit: str):
    if unit not in UNIT_GROUPS:
        raise InvalidUnitError(unit)

def check_incompetible_units(unit1: str, unit2: str):
    if UNIT_GROUPS[unit1] != UNIT_GROUPS[unit2]:
        raise IncompetibleUnitsError(unit1, unit2)

def check_value(value: str):
    try:
        float_value = float(value)
        if isnan(float_value):
            raise InvalidValueError(value)
    except ValueError:
        raise InvalidValueError(value)
