from toolkit.calc_validation import validate_calculator
from toolkit.tokenizer import tokenize, mark_unary_operators, Token
from toolkit.errors import CalculatorError, ZeroDivError, FloatSpecialDivError
from toolkit.constants import OP_PRIORITY, UNARY_PRIORITY


# Функция получения приоритета операции для сортировочной станции
def get_priority(operator: Token) -> int:
    """ Получение приоритета
        Функция получает  на вход оператор и возвращает его приоритет
        
        Args:
            token: оператор в формате токена
        
        Returns:
            Приоритет операции от 0 до 2
    """
    if operator.token_type == "UOPERATION":
        return UNARY_PRIORITY
    return OP_PRIORITY[operator.data]

# Вспомогательная функция для примененяи операций при подсчете rpn
def apply_operation(num1: Token, num2: Token, operation: str) -> Token:
    """Выполнение операции
        Выполняет нужно операцию к двум числам. Является вспомогательной функцией
        для функции rpn_to_result

    Args:
        num1: Первый операнд в формате токена
        num2: Второй операнд в формате токена
        operation: Оператор в формате строки: "+"/"-"/...

    Raises:
        FloatSpecialDivError: Если в спец. делении учавствует число в формате float

    Returns:
        Токен с результатом вычисления
    """
    if operation in ["//", "%"] and (type(num1.data) != int or type(num2.data) != int):
        raise FloatSpecialDivError()
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
    """Реализация стэка
    Attributes:
        items: список, в котором лежат все эелементы стэка
    """
    def __init__(self):
        self.items = []
    
    def __iter__(self):
        return iter(reversed(self.items))
    
    def peek(self):
        """Получение верхнего элемента стэка"""
        return self.items[-1]

    def push(self, item):
        """Добавление элемента в стэк"""
        self.items.append(item)

    def pop(self):
        """Удаление верхнего элемента из стэка"""
        return self.items.pop()

    def is_empty(self):
        """Проверка стэка на пустоту внетри"""
        return (self.items == [])
    
    def lenth(self):
        """Получение длинны стэка"""
        return len(self.items)

# Главная входная точка всей программы-калькулятора
def calc_manager(example: str) -> float | int:
    """Главная входная точка всей программы-калькулятора
    Является центром калькулятора, вызывает все функции

    Args:
        example: выраженеи в формате str

    Returns:
        Результат вычисления
    """
    # Перевод в токены
    tokenized_example = tokenize(example)
    mark_unary_operators(tokenized_example)
    
    # Валидация
    validate_calculator(tokenized_example)
    
    # Перевод в rpn
    rpn_example = example_to_rpn(tokenized_example)
    # Получение результата из rpn
    result = rpn_to_result(rpn_example)
    
    return result

def example_to_rpn(tokenized_example: list) -> list:
    """Превращение выражения в rpn
        Переводит обычное окенизированное выражение в rpn при помощи 
        алгоритма сортировочной станции Дейкстры

    Args:
        tokenized_example: Токенизированное выражение

    Returns:
        Выражение в виде обратной польской нотации
    """
    rpn_result = []
    stack = Stack()
    
    for token in tokenized_example:
        if token.token_type == "NUM":
            rpn_result.append(token)
            
        elif token.token_type == "LPAREN":
            stack.push(token)
            
        elif token.token_type == "OPERATION":
            # Вытаскивание операторов из стэка, пока приоритет не будет ниже текущего оператора
            while (not stack.is_empty() and (stack.peek().token_type == "OPERATION" or
                    stack.peek().token_type == "UOPERATION")
                    and get_priority(stack.peek()) >= get_priority(token)):
                rpn_result.append(stack.pop())
                
            stack.push(token)
        
        elif token.token_type == "UOPERATION":
            # Вытаскивание операторов из стэка, пока приоритет не будет ниже текущего оператора
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
def rpn_to_result(tokenized_example: list) -> float | int:
    """Вычисляет результат выражения в rpn
        Считает результат выражения алгоритмом вычисления с помощью стэка

    Args:
        tokenized_example: Токенизированное выражение

    Raises:
        ZeroDivError: Если происходит попытка деленяи на ноль
        CalculatorError: Базовая ошибка калькулятора

    Returns:
        Результат вычисления выражения
    """
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
            if operation in ["/", "//", "%"] and num1.data == 0:
                raise ZeroDivError()
            
            stack.push(apply_operation(num1, num2, token.data))
            
    if stack.lenth() == 1:
        return stack.peek().data
    else:
        raise CalculatorError("В стэке остались значения: выражение написано с ошибкой")
            