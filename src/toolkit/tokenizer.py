from typing import Union

from dataclasses import dataclass

from re import finditer, compile, VERBOSE

OPERATIONS = {
    "PLUS": "+",
    "MINUS": "-",
    "MUL": "*",
    "DIV": "/"
}

@dataclass
class Token():
    # Аннотация для dataclass
    token_type: str
    data: Union[None, float] = None

def tokenizer(example):     # TODO: сделать проверку на нормальное кол-во скобок
    # Паттерн токенизации
    TOKEN_PATTERN = compile(r"""
    (?P<NUM>\d+(\.\d+)?) |
    (?P<PLUS>\+) |
    (?P<MINUS>-) |
    (?P<MUL>\*) |
    (?P<DIV>/) |
    (?P<LPAREN>\() |
    (?P<RPAREN>\)) |
    (?P<OMISSION>\s+) |
    (?P<UNKNOWN>.)
    """, VERBOSE)
    
    tokenised_example = []
    
    tokens = finditer(TOKEN_PATTERN, example)
    
    for i in tokens:
        token_type = i.lastgroup
        data = i.group()

        if token_type == "OMISSION":
            continue
        elif token_type == "UNKNOWN":
            print("UNKNOWN!!!")
            continue # TODO: Сделать вызов ошибки
        
        if token_type == "NUM":
            tokenised_example.append(Token(token_type, float(data)))
        elif token_type in OPERATIONS.keys():
            tokenised_example.append(Token("OPERATION", OPERATIONS.get(token_type)))
        else:
            tokenised_example.append(Token(token_type))
    
    return tokenised_example
    
if __name__ == "__main__":
    print(tokenizer("(-1 +    1) /3.53  * 456"))
