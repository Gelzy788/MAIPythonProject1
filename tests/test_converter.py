import pytest

from toolkit.converter import converter_manager
from toolkit.errors import TemperatureBelowAbsZero


@pytest.mark.parametrize(
    "value, frm, to, expected",
    [
        ("1", "km", "m", 1000),
        ("1500", "mm", "m", 1.5),
        ("1", "m", "cm", 100),
        ("250", "cm", "km", 0.0025),
        ("5", "m", "m", 5),
    ],
)
def test_length(value, frm, to, expected):
    """Перевод длинны"""
    assert converter_manager(value, frm, to) == pytest.approx(expected)


@pytest.mark.parametrize(
    "value, frm, to, expected",
    [
        ("2.5", "kg", "g", 2500),
        ("500", "g", "kg", 0.5)
    ]
)
def test_mass(value, frm, to, expected):
    """Перевод массы"""
    assert converter_manager(value, frm, to) == pytest.approx(expected)


@pytest.mark.parametrize(
    "value, frm, to, expected",
    [
        ("0", "c", "f", 32),
        ("100", "c", "f", 212),
        ("0", "c", "k", 273.15),
        ("0", "k", "c", -273.15),
        ("32", "f", "c", 0),
        ("-40", "c", "f", -40),
    ],
)
def test_temperature(value, frm, to, expected):
    """Перевод температуры"""
    assert converter_manager(value, frm, to) == pytest.approx(expected)


@pytest.mark.parametrize(
    "value, unit", [("-300", "c"), ("-1", "k"), ("-500", "f")])
def test_below_absolute_zero(value, unit):
    """Температура ниже абсолютного нуля"""
    with pytest.raises(TemperatureBelowAbsZero):
        converter_manager(value, unit, "k")