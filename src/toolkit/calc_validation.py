from toolkit.errors import (
    EmptyExpressionError,
    InvalidSymbolError,
    MissingOperandError,
    MissingOperatorError,
    TwoOperatorsInRowError,
    UnbalancedParenthesesError,
)

def validate_calculator(tokenized_example):
    """Менеджер валидации калькулятора
    
        Вызывает все функции, связанные с валидацией калькулятора
            и является единой точкой входа на данный этап
        
        Args:
            tokenized_example: Токенизированное выражение в формате спика
    """
    check_empty(tokenized_example)
    check_unknown_symbols(tokenized_example)
    check_paren_balance(tokenized_example)
    check_example_structure(tokenized_example)

# Проверка, заполнено ли выражение
def check_empty(tokenized_example: list):
    """Проверяет выражение на пустоту
        Проверяет, не ввел ли пользователь пустое выражение.
        Если ввел - вызывает ошибку
        
        Args:
            tokenized_example: Токенизированное выражение в формате спика
        
        Raises:
            EmptyExpressionError: Если выражение пустое
    """
    if len(tokenized_example) == 0:
        raise EmptyExpressionError

# Проверка на неизвестные символы
def check_unknown_symbols(tokenized_example: list):
    """ Проверка на неизвестные символы
        Ищет среди токенов те, что с типом UNKNOWN 
        при нахождении вызывает ошибку
        
        Args:
            tokenized_example: Токенизированное выражение в формате спика
        
        Raises:
            InvalidSymbolError - Если в выражении неизвестный символ
    """
    for pos, token in enumerate(tokenized_example):
        if token.token_type == "UNKNOWN":
            raise InvalidSymbolError(token.data, pos)

# Проверка баланска скобок
def check_paren_balance(tokenized_example: list):
    """Проверка скобок
        Проверяет правильность постановки скобок:
        их количество и последовательность
        
        Args:
            tokenized_example: Токенизированное выражение в формате спика
            
        Raises:
            UnbalancedParenthesesError - Если баланс скобок не соблюден
    """
    balance = 0
    for pos, token in enumerate(tokenized_example):
        if token.token_type == "LPAREN":
            balance += 1
        elif token.token_type == "RPAREN":
            balance -= 1
            if balance < 0:
                raise UnbalancedParenthesesError()
    if balance != 0:
        raise UnbalancedParenthesesError()

# Проверка правильности постановки операторов
def check_example_structure(tokenized_example: list):
    """ Проверяет структуру выражения
        Првоеряет пропущеные операнды и операторы,
        а также два неунарных оператора подряд
        Алгоритм проходится по все выражению и делает проверки в зависимости от статуса:
            0 — поиск начала операнда
            1 — поиск числа сразу после унарного оператора
            2 — поиск оператора или ) после числа
        При несоответствии следующего элемента статусу вызывает соответствующую ошибку

    Args:
        tokenized_example: Токенизированное выражение в формате спика

    Raises:
        TwoOperatorsInRowError: Если стоит два неунарных оператора подряд
        MissingOperatorError: Если между операндами пропущен оператор
        MissingOperandError: Если пропущен операнд после оператора
    """
    state = 0

    for position, token in enumerate(tokenized_example):
        # Ищем начало операнда
        if state == 0:
            if token.token_type == "NUM":
                state = 2
            elif token.token_type == "LPAREN":
                pass
            elif token.token_type == "UOPERATION":
                state = 1
            elif token.token_type == "OPERATION" and position > 0 \
                    and tokenized_example[position - 1].token_type == "OPERATION":
                raise TwoOperatorsInRowError(position)
            else:
                raise MissingOperandError(position)

        # Если прошлым мыл унарный оператор
        elif state == 1:
            if token.token_type == "NUM":
                state = 2
            elif token.token_type == "LPAREN":
                state = 0
            elif token.token_type == "OPERATION":
                raise TwoOperatorsInRowError(position)
            else:
                raise MissingOperandError(position)

        # Если прошлым было число
        elif state == 2:
            if token.token_type == "OPERATION":
                state = 0
            elif token.token_type == "RPAREN":
                pass
            else:
                # число или "(" сразу после числа / ")"
                raise MissingOperatorError(position)

    # выражение не должно заканчиваться оператором
    if state != 2:
        raise MissingOperandError(len(tokenized_example))
