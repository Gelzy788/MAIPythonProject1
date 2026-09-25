from dataclasses import dataclass
from re import finditer

from toolkit.constants import OPERATIONS, TOKEN_PATTERN


@dataclass
class Token:
    """Класс токена
    
        Хранит в себе два поля: тип токена и его значение. Тип токена всегда в str и
        пишется заглавными буквами(Например NUM, LPAREN, OPERATION).
        Значение токена может быть None, float, int и str, в зависимости от типа токена:
            NUM: int|float
            RPAREN: None
            LPAREN: None
            UNKNOWN: None
            OPERATION: str
        
        token_type: Тип токена
        data: Значение токена
    """
    token_type: str
    data: None | float | int | str = None

def tokenize(example: str) -> list:
    """Токенизатор
    
        Токенизирует выражение, поданное на вход, выдавая список токенов игнорирует пробелы

    Args:
        example: Выражение

    Returns:
        Токинизированное выражение: список токенов
    """
    tokenised_example = []
    
    tokens = finditer(TOKEN_PATTERN, example)
    for i in tokens:
        token_type = i.lastgroup
        data = i.group()

        if token_type == "OMISSION":
            continue
        elif token_type == "UNKNOWN":
            tokenised_example.append(Token(token_type, None))
        
        elif token_type == "NUM":
            if "." in data:
                tokenised_example.append(Token(token_type, float(data)))
            else:
                tokenised_example.append(Token(token_type, int(data)))
                
        elif token_type in OPERATIONS.keys():
            tokenised_example.append(Token("OPERATION", OPERATIONS.get(token_type)))
        else:
            tokenised_example.append(Token(token_type))
    
    return tokenised_example

def mark_unary_operators(tokenized_example: list):
    """Нахождение унарных операторов
    
        Ищет унарные операторы и меняет их тип класса с OPERATION на UOPERATION

    Args:
        tokenized_example: Токенизированное выражение 
    """
    
    for i in range(len(tokenized_example)):
        if (tokenized_example[i].token_type == "OPERATION"
            and tokenized_example[i].data in "+-" and (i == 0
            or tokenized_example[i-1].token_type == "LPAREN"
            or tokenized_example[i-1].token_type == "OPERATION")):
                tokenized_example[i].token_type = "UOPERATION"