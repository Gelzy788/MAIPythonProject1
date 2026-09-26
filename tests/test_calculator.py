import pytest

from toolkit.calculator import calc_manager
from toolkit.errors import FloatSpecialDivError, ZeroDivError


@pytest.mark.parametrize(
    "expr, result",
    [
        ("2 + 3", 5),
        ("10 - 4", 6),
        ("6 * 7", 42),
        ("10 / 4", 2.5),
        ("  9 ", 9),
        ("2 + 2 * 2", 6),
        ("(2 + 2) * 2", 8),
        ("1.5 * 2", 3),
        ("0.1 + 0.2", 0.3),
        ("-5 + 3", -2),
        ("-5 + +5", 0),
        ("7 // 2", 3),
        ("7 % 3", 1)
    ],
)
def test_positive_calc(expr, result):
    """Позитивные тесты калькулятора"""
    assert calc_manager(expr) == pytest.approx(result)

@pytest.mark.parametrize(
    "expr", ["10 // 0", "4 % 0", "1 / 0", "4 // (2 - 2)"])
def test_zero_div(expr):
    """Деление на ноль"""
    with pytest.raises(ZeroDivError):
        calc_manager(expr)

@pytest.mark.parametrize(
    "expr", ["10.0 // 4", "10.0 % 4", "(2.5 * 4) // 8", "7.4 % 6"])
def test_float_cpecial_div(validate_calc, expr):
    """Спец. деление float """
    with pytest.raises(FloatSpecialDivError):
        calc_manager(expr)