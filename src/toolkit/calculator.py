from tokenizer import Token, tokenizer

OP_PRIORITY = {
    "+": 0,
    "-": 0,
    "*": 1,
    "/": 1,
    "%": 1,
    "//": 1,
}

class Stack:
    def __init__(self):
        self.items = []
        
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

def manager(example):   # FIXME: Нет никакой проверки на два идущих подряд неунарных оператор(напрмиер /* или +/)
    # Перевод в токены
    example = tokenizer(example)
    paren_balance_check(example)
    rpn_example = example_to_rpn(example)
    return rpn_example
    result = rpn_to_result(rpn_example)
    
    # TODO: Запись в json
    
    return result

def paren_balance_check(example):   #FIXME: сейчас функция првоеряет только кол-во скобок, так что есть будет )(, то ошибки не будет
    rparen_count = 0
    lparen_count = 0
    for i in example:
        if i.token_type == "LPAREN":
            lparen_count += 1
        elif i.token_type == "RPAREN":
            rparen_count += 1
    if rparen_count != lparen_count:
        #TODO: сделать вызов ошибки баланса скобок
        print("БАЛАНС СКОБОК НЕ СОБЛЮДЕН")
        exit(0)

def example_to_rpn(example):
    rpn_result = []
    stack = Stack()
    
    for token in example:
        if token.token_type == "NUM":
            rpn_result.append(token)
        elif token.token_type == "LPAREN":
            stack.push(token)
        elif token.token_type == "OPERATION":
            while (not stack.is_empty() and stack.peek().token_type == "OPERATION" 
                    and OP_PRIORITY[stack.peek().data] >= OP_PRIORITY[token.data]):
                rpn_result.append(stack.pop())
            stack.push(token)
        elif token.token_type == "RPAREN":
            while (not stack.is_empty() and stack.peek().token_type != "LPAREN"):
                rpn_result.append(stack.pop())
            stack.pop()
    while not stack.is_empty():
        rpn_result.append(stack.pop())
    return rpn_result

def rpn_to_result(example):
    pass

if __name__ == "__main__":
    example = "(1 +    1) /3.53  * 456 + 5"
    print(manager(example))