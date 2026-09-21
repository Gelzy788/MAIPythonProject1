from toolkit.validation import validate_manager
from toolkit.tokenizer import tokenize, mark_unary_operators
from toolkit.tokenizer import Token
from toolkit.errors import CalculatorError, ZeroDivError

# Словарь с приоритетами различных операций(кроме унарных)
OP_PRIORITY = {
    "+": 0,
    "-": 0,
    "*": 1,
    "/": 1,
    "%": 1,
    "//": 1,
}

UNARY_PRIORITY = 2  # Константа приоритета для унарных операций

# Функция получения приоритета операции для сортировочной станции
def get_priority(token):
    if token.token_type == "UOPERATION":
        return UNARY_PRIORITY
    return OP_PRIORITY[token.data]

# Вспомогательная функция для примененяи операций при подсчете rpn
def apply_operation(num1, num2, operation):
    if operation == "+":
        res = num2.data + num1.data
    elif operation == "-":
        res = num2.data - num1.data
    elif operation == "/":
        res = num2.data / num1.data
    elif operation == "*":
        res = num2.data * num1.data
    elif operation == "//":
        res = num2.data // num1.data
    elif operation == "%":
        res = num2.data % num1.data
    return Token("NUM", res)

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

# Главная входная точка всей программы-калькулятора
def calc_manager(example):
    # Перевод в токены
    tokenized_example = tokenize(example)
    mark_unary_operators(tokenized_example)
    
    # Валидация
    validate_manager(tokenized_example)
    
    # Перевод в rpn
    rpn_example = example_to_rpn(tokenized_example)
    print(rpn_example)
    # return rpn_example

    # Получение результата из rpn
    result = rpn_to_result(rpn_example)
    
    # TODO: Запись в json
    
    return result

# Превращение выражения в rpn по алгоритму сортировочной станции Дейкстры
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

# Подсчет rpn в результат
def rpn_to_result(tokenized_example):
    stack = Stack()
    for token in tokenized_example:
        if token.token_type == "NUM":
            stack.push(token)
        elif token.token_type == "UOPERATION":
            if token.data == "-":
                stack.peek().data *= -1
        else:
            num1, num2 = stack.pop(), stack.pop()
            operation = token.data
            
            #  Отлавливаем ошибку деления на 0
            print(f"num1:{num1.data} \t num2: {num2.data}\t op: {operation}")
            if operation in ["/", "//", "%"] and num1.data == 0:
                raise ZeroDivError()
            
            stack.push(apply_operation(num1, num2, token.data))
    if stack.lenth() == 1:
        return stack.peek().data
    else:
        raise CalculatorError("В стэке остались значения: выражение написано с ошибкой")
            

if __name__ == "__main__":
    example = "(1 +    1) /(1-1)  * 456 + 5"
    print(calc_manager(example))