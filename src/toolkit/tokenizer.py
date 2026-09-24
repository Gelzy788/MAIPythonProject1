from typing import Union

from dataclasses import dataclass

from re import finditer

from toolkit.constants import TOKEN_PATTERN, OPERATIONS

@dataclass
class Token():
    # Аннотация для dataclass
    token_type: str
    data: Union[None, float, int, str] = None

def tokenize(example):
    tokenised_example = []
    
    tokens = finditer(TOKEN_PATTERN, example)
    for i in tokens:
        token_type = i.lastgroup
        data = i.group()

        if token_type == "OMISSION":
            continue
        elif token_type == "UNKNOWN":
            tokenised_example.append(Token(token_type, data))
        
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

def mark_unary_operators(tokenized_example):
    for i in range(len(tokenized_example)):
        if (tokenized_example[i].token_type == "OPERATION"
            and tokenized_example[i].data in "+-" and (i == 0
            or tokenized_example[i-1].token_type == "LPAREN"
            or tokenized_example[i-1].token_type == "OPERATION")):
                tokenized_example[i].token_type = "UOPERATION"