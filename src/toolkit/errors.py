class CalcConverterError(Exception):
    # Базова ошибка всей программы
    pass

class CalculatorError(CalcConverterError):
    # Базовая ошибка для калькулятор
    pass

class ConverterError(CalcConverterError):
    # Базовая ошибка для конвертера
    pass

class FloatSpecialDivError(CalculatorError):
    def __init__(self):
        """Ошибка при попытке  применения спец. деления с float"""
        super().__init__("Операторы // и % не могут взаимодействовать" +
                        "с числами с запятой")

class EmptyExpressionError(CalculatorError):
    """Ошибка при пустом выражении на входе в калькулятор"""
    def __init__(self):
        super().__init__("Пустое выражение")
    
class InvalidSymbolError(CalculatorError):
    """Ошибка неизвестного символа в выражении"""
    def __init__(self, symbol: str, position: int):
        super().__init__("В выражении неизвестный символ " +
                        f"'{symbol}' на позиции {position}")

class MissingOperatorError(CalculatorError):
    """Ошибка пропущенного оператора в выражении"""
    def __init__(self, position: int):
        super().__init__(f"В выражении пропущен оператор на позиции {position}")

class MissingOperandError(CalculatorError):
    """Ошибка пропущенного операнда в выражении"""
    def __init__(self, position: int):
        super().__init__(f"В выражении пропущен операнд на позиции {position}")

class TwoOperatorsInRowError(CalculatorError):
    """Ошибка двух неунарных операторов подряд в выражении"""
    def __init__(self, position: int):
        super().__init__(f"Два оператора подряд на позиции {position}")

class UnbalancedParenthesesError(CalculatorError):
    """Ошибка нарушения баланса скобок в выражении"""
    def __init__(self):
        super().__init__("В выражении несбалансирвоанное кол-во скобок")

class ZeroDivError(CalculatorError):
    """Ошибка деления на ноль"""
    def __init__(self):
        super().__init__("В выражении присутствует деление на ноль")

class InvalidUnitError(ConverterError):
    """Ошибка неизвестной величины в конвертере"""
    def __init__(self, unknown_unit: str):
        super().__init__(f"На вход подана неизвестная единица: {unknown_unit}")

class IncompetibleUnitsError(ConverterError):
    """Ошибка несовместимых величин"""
    def __init__(self, unit1: str, unit2: str):
        super().__init__("На вход программы поданы несовместимые единицы:" +
                        f"{unit1}, {unit2}")

class InvalidValueError(ConverterError):
    """Ошибка неправильного ввода числа в конвертер"""
    def __init__(self, value: float):
        super().__init__(f"Неправильно записано число: {value}")

class TemperatureBelowAbsZero(ConverterError):
    """Ошибка ввода температуры ниже абсолютного нуля"""
    def __init__(self):
        super().__init__("Температура не может быть ниже абсолютного нуля")

class HistorySaveError(CalcConverterError):
    """Ошибка сохранения истории вычислений"""
    def __init__(self):
        super().__init__("Произошла ошибка сохранения истории")
