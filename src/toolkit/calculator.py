from tokenizer import Token, tokenizer

OP_PRIORITY = {
    "+": 0,
    "-": 0,
    "*": 1,
    "/": 1,
    "%": 1,
    "//": 1,
}

UNARY_PRIORITY = 2

def get_priority(token):
    if token.token_type == "UOPERATION":
        return UNARY_PRIORITY
    return OP_PRIORITY[token.data]

class Stack:
    def __init__(self):
        self.items = []
    
    def __iter__(self):
        return iter(reversed(self.items))
    
    def peek(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])
    
    def lenth(self):
        return len(self.items)

def calc_manager(example):
    # Перевод в токены
    example = tokenizer(example)

    rpn_example = example_to_rpn(example)
    return rpn_example
    result = rpn_to_result(rpn_example)
    
    # TODO: Запись в json
    
    return result

def example_to_rpn(tokenized_example):
    rpn_result = []
    stack = Stack()
    
    for token in tokenized_example:
        if token.token_type == "NUM":
            rpn_result.append(token)
        elif token.token_type == "LPAREN":
            stack.push(token)
        elif token.token_type == "OPERATION":
            while (not stack.is_empty() and (stack.peek().token_type == "OPERATION" or
                    stack.peek().token_type == "UOPERATION")
                    and get_priority(stack.peek()) >= get_priority(token)):
                rpn_result.append(stack.pop())
            stack.push(token)
        elif token.token_type == "UOPERATION":
            while (not stack.is_empty() and (stack.peek().token_type == "OPERATION" or
                    stack.peek().token_type == "UOPERATION")
                    and get_priority(stack.peek()) > get_priority(token)):
                rpn_result.append(stack.pop())
            stack.push(token)
        elif token.token_type == "RPAREN":
            while (not stack.is_empty() and stack.peek().token_type != "LPAREN"):
                rpn_result.append(stack.pop())
            stack.pop()
    while not stack.is_empty():
        rpn_result.append(stack.pop())
    return rpn_result

def rpn_to_result(tokenized_example):
    pass

if __name__ == "__main__":
    example = "(1 +    1) /3.53  * 456 + 5"
    print(calc_manager(example))