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
    # EXPECT_OPERAND        — поиск начала операнда
    # EXPECT_OPERAND_STRICT — поиск числа сразу после унарного оператора
    # EXPECT_OPERATOR       — поиск оператора или ) после числа
    state = "EXPECT_OPERAND"

    for position, token in enumerate(tokens):
        if state == "EXPECT_OPERAND":
            if token.token_type == "NUM":
                state = "EXPECT_OPERATOR"
            elif token.token_type == "LPAREN":
                pass  # состояние не меняется
            elif token.token_type == "UOPERATION":
                state = "EXPECT_OPERAND_STRICT"
            else:
                raise MissingOperandError(position)
            
        elif state == "EXPECT_OPERAND_STRICT":
            if token.token_type == "NUM":
                state = "EXPECT_OPERATOR"
            elif token.token_type == "LPAREN":
                state = "EXPECT_OPERAND"
            elif token.token_type == "UOPERATION":
                raise TwoOperatorsInRowError(position)  # цепочка унарных
            else:
                raise MissingOperandError(position)

        elif state == "EXPECT_OPERATOR":
            if token.token_type == "OPERATION":
                state = "EXPECT_OPERAND"
            elif token.token_type == "RPAREN":
                pass
            else:
                raise TwoOperatorsInRowError(position)

    if state != "EXPECT_OPERATOR":
        raise MissingOperandError(len(tokens))