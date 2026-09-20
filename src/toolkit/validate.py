from errors import *

def validate_manager(tokenized_example):
    check_empty(tokenized_example)
    check_unknown_symbols(tokenized_example)
    check_paren_balance(tokenized_example)
    check_operators(tokenized_example)

# Проверка, заполнено ли выражение
def check_empty(tokenized_example):
    if len(tokenized_example) == 0:
        raise EmptyExpressionError

# Проверка на неизвестные символы
def check_unknown_symbols(tokenized_example):
    for pos, token in enumerate(tokenized_example):
        if token.token_type == "UNKNOWN":
            raise InvalidSymbolError(token.data, pos)

# Проверка баланска скобок
def check_paren_balance(tokenized_example):
    balance = 0
    for pos, token in enumerate(tokenized_example):
        if token.token_type == "LPAREN":
            balance += 1
        elif token.token_sype == "RPAREN":
            balance -= 1
            if balance < 0:
                raise UnbalancedParenthesesError()
    if balance != 0:
        raise UnbalancedParenthesesError()

# Проверка правильности постановки операторов
def check_operators(tokens):
    # 0 — поиск начала операнда
    # 1 — поиск числа сразу после унарного оператора
    # 2       — поиск оператора или ) после числа
    state = 0

    for position, token in enumerate(tokens):
        if state == 0:
            if token.token_type == "NUM":
                state = 1
            elif token.token_type == "LPAREN":
                pass  # состояние не меняется
            elif token.token_type == "UOPERATION":
                state = 1
            else:
                raise MissingOperandError(position)
            
        elif state == 1:
            if token.token_type == "NUM":
                state = 1
            elif token.token_type == "LPAREN":
                state = 0
            elif token.token_type == "UOPERATION":
                raise TwoOperatorsInRowError(position)  # цепочка унарных
            else:
                raise MissingOperandError(position)

        elif state == 1:
            if token.token_type == "OPERATION":
                state = 0
            elif token.token_type == "RPAREN":
                pass
            else:
                raise TwoOperatorsInRowError(position)

    if state != 1:
        raise MissingOperandError(len(tokens))