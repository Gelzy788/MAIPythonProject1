class CalculatorError(Exception):
    # Базовая ошибка для калькулятор
    pass

class ConverterError(Exception):
    # Базовая ошибка для конвертера
    pass

class FloatSpecialDivError(CalculatorError):
    def __init__(self):
        super().__init__("Операторы // и % не могут взаимодействовать" +
                        "с числами с запятой")

class EmptyExpressionError(CalculatorError):
    def __init__(self):
        super().__init__("Пустое выражение")
    
class InvalidSymbolError(CalculatorError):
    def __init__(self, symbol, position):
        super().__init__("В выражении неизвестный символ" + 
                        f"{symbol} на позиции {position}")

class MissingOperatorError(CalculatorError):
    def __init__(self, position):
        super().__init__(f"В выражении пропущен оператор на позиции {position}")

class MissingOperandError(CalculatorError):
    def __init__(self, position):
        super().__init__(f"В выражении пропущен операнд на позиции {position}")

class TwoOperatorsInRowError(CalculatorError):
    def __init__(self, position):
        super().__init__(f"Два оператора подряд на позиции {position}")

class UnbalancedParenthesesError(CalculatorError):
    def __init__(self):
        super().__init__("В выражении несбалансирвоанное кол-во скобок")

class ZeroDivError(CalculatorError):
    def __init__(self):
        super().__init__("В выражении присутствует деление на ноль")

class InvalidUnitError(ConverterError):
    def __init__(self, unknown_unit: str):
        super().__init__(f"На вход подана неизвестная единица: {unknown_unit}")

class IncompetibleUnitsError(ConverterError):
    def __init__(self, unit1, unit2):
        super().__init__("На вход программы поданы несовместимые единицы:" +
                        f"{unit1}, {unit2}")

class InvalidValueError(ConverterError):
    def __init__(self, value):
        super().__init__(f"Неправильно записано число: {value}")

class TemperatureBelowAbsZero(ConverterError):
    def __init__(self):
        super().__init__("Температура не может быть ниже абсолютного нуля")
