import pytest

from toolkit.errors import (
    IncompetibleUnitsError,
    InvalidUnitError,
    InvalidValueError,
)


@pytest.mark.parametrize(
    "value, from_unit, to_unit", [(30, "mm", "lm"), (30, "ndmc", "mm")])
def test_invalid_unit(value, from_unit, to_unit, validate_converter):
    """Неизместная величина"""
    with pytest.raises(InvalidUnitError):
        validate_converter(value, from_unit, to_unit)

@pytest.mark.parametrize(
    "value, from_unit, to_unit", [("ajd", "mm", "km"), ("NaN", "mm", "km")])
def test_invalid_value(value, from_unit, to_unit, validate_converter):
    "Неправильно введено число"
    with pytest.raises(InvalidValueError):
        validate_converter(value, from_unit, to_unit)

@pytest.mark.parametrize(
    "value, from_unit, to_unit", [(53, "mm", "f"), (48, "f", "kg")])
def test_incompetible_units(value, from_unit, to_unit, validate_converter):
    """Несовместимые величины"""
    with pytest.raises(IncompetibleUnitsError):
        validate_converter(value, from_unit, to_unit)