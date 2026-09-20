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

def tokenizer(example):
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
            tokenised_example.append(Token(token_type, data))
        
        if token_type == "NUM":
            tokenised_example.append(Token(token_type, float(data)))
        elif token_type in OPERATIONS.keys():
            tokenised_example.append(Token("OPERATION", OPERATIONS.get(token_type)))
        else:
            tokenised_example.append(Token(token_type))
    
    return tokenised_example

def mark_unary_operators(tokenized_example):
    for i in range(len(tokenized_example)):
        if tokenized_example[i].token_type == "OPERATION" and tokenized_example[i].data in "+-" and (i == 0 
            or tokenized_example[i-1].token_type == "LPAREN"
            or tokenized_example[i-1].token_type == "OPERATION"):
                tokenized_example[i].token_type = "UOPERATION"
    
if __name__ == "__main__":
    print(tokenizer("(-1 +    1) /3.53  * 456"))
