import pytest

from toolkit.errors import (
    EmptyExpressionError,
    InvalidSymbolError,
    MissingOperandError,
    MissingOperatorError,
    TwoOperatorsInRowError,
    UnbalancedParenthesesError,
)


@pytest.mark.parametrize(
    "expr", ["5 + 7", "-2*4", "(5 + 7) * 4", "-3", "10 // 3 % 5"])
def test_good_expression(validate_calc, expr):
    """Успешная валидация"""
    validate_calc(expr)

@pytest.mark.parametrize("expr", ["", "     "])
def test_empty_expr(validate_calc, expr):
    """Пустое выражение"""
    with pytest.raises(EmptyExpressionError):
        validate_calc(expr)

@pytest.mark.parametrize("expr", ["2@3", "erf"])
def test_invalid_symbol(validate_calc, expr):
    """Неизвестный символ"""
    with pytest.raises(InvalidSymbolError):
        validate_calc(expr)

@pytest.mark.parametrize("expr", ["2 +", "2 + -", "* 5", "()"])
def test_missing_operand(validate_calc, expr):
    """Пропущен операнд"""
    with pytest.raises(MissingOperandError):
        validate_calc(expr)

@pytest.mark.parametrize("expr", ["2 3", "2 (3 * 4)"])
def test_missing_operator(validate_calc, expr):
    """Пропущен оператор"""
    with pytest.raises(MissingOperatorError):
        validate_calc(expr)

@pytest.mark.parametrize("expr", ["3 +* 9", "2 -- -5"])
def test_two_operators_in_row(validate_calc, expr):
    """Два оператора подряд"""
    with pytest.raises(TwoOperatorsInRowError):
        validate_calc(expr)

@pytest.mark.parametrize("expr", ["2 - 5)", ") 2 (", "((5 - 2)", "(2 - 5"])
def test_unbalanced_parentheses(validate_calc, expr):
    """Несбалансированное кол-во скобок"""
    with pytest.raises(UnbalancedParenthesesError):
        validate_calc(expr)