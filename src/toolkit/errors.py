class CalculatorError(Exception):
    # Базовая ошибка для калькулятор
    pass

class ConverterError(Exception):
    # Базовая ошибка для конвертера
    pass

class EmptyExpressionError(CalculatorError):
    def __init__(self):
        super().__init__("Пустое выражение")
    
class InvalidSymbolError(CalculatorError):
    def __init__(self, symbol, position):
        super().__init__(f"В выражении неизвестный символ {symbol} на позиции {position}")

class MissingOperatorError(CalculatorError):
    def __init__(self, position):
        super().__init__(f"В выражении пропущен оператор на позиции {position}")

class TwoOperatorsInRowError(CalculatorError):
    def __init__(self):
        super().__init__("Два оператора подряд на позиции {position}")

class UnbalancedParenthesesError(CalculatorError):
    def __init__(self):
        super().__init__("В выражении несбалансирвоанное кол-во скобок")

class ZeroDivError(CalculatorError):
    def __init__(self):
        super().__init__("В выражении присутствует деление на ноль")

class InvalidUnitError(ConverterError):
    def __init__(self, unknown_unit: str):
        super().__init__(f"На вход подана неизвестная единица: {unknown_unit}")

class IncompatibleUnitsError(ConverterError):
    def __init__(self):
        super().__init__("На входи программы поданы несовместимые единицы")

class InvalidValueError(ConverterError):
    def __init__(self, value):
        super().__init__(f"Неправильно записано число: {value}")