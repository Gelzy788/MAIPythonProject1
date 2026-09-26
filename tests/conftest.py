import pytest

from toolkit.calc_validation import validate_calculator
from toolkit.converter_validation import validate_converter as _validate_converter
from toolkit.tokenizer import mark_unary_operators, tokenize


@pytest.fixture
def validate_calc():
    """Токенизирует и валидирует выражение, не вычисляя его."""

    def _validate(expression: str):
        tokens = tokenize(expression)
        mark_unary_operators(tokens)
        validate_calculator(tokens)

    return _validate


@pytest.fixture
def validate_converter():
    """Вызывает валидацию конвертера, перед этим приводя единицы к нижнему регистру."""

    def _validate(value: str, from_unit: str, to_unit: str):
        _validate_converter(value, from_unit.lower(), to_unit.lower())

    return _validate
    
