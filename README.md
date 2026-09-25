# Программирование на Python. Лабораторная работа №1

Консольный калькулятор и конвертер величин

#### В программе реализованы следующие блоки:
**калькулятор поддерживает:**
* Следующие операции: *,/,//,%,+,-
* Скобки и учитывает приоритеты операций
* Унарные операторы

**конвертер поддерживает:**
* Длинна: mm, cm, m, km
* Масса: g, kg
* Температура: c(Цельсии), f(Фаренгейты), k(Кельвины) (Температура не должна быть ниже абсолютного нуля)

**Сохранение истории успешных операций:**
* История лежит в файле logs/history.json

### Структура проекта
```
|- src/toolkit/
|       |- __init__.py
|       |- __main__.py - Точка входа всей программы
|       |- calc_validation.py - Валидация калькулятора
|       |- calculator.py - Функционал калькулятора(Перевод в rpn и подсчет)
|       |- constants.py - Служебные программы для всей программы
|       |- converter_validation.py - Валидация конвертера
|       |- converter.py - Функционал конвертера
|       |- errors.py - Самописные ошибки
|       |- history_saver.py - Функционал сохранения истории успешных операций в logs/history.json
|       |- tokenizer.py - Токенизатор выраженяи для калькулятора
|       |- units.json - Конфигурационный файл с коэффициентами 
```

### Команды запуска
```bash
python -m toolkit calc "EXPRESSION"
python -m toolkit convert VALUE --from UNIT --to UNIT
python -m toolkit --help
```

### Возможные ошибки
**Калькулятор:**
* FloatSpecialDivError - Попытка использования спец деления(//, %) со значениями с запятой
* EmptyExpressionError - Подано пустое выражение на вход
* InvalidSymbolError - Неизвестный символ в выражении
* MissingOperatorError - В выражении пропущен оператор
* MissingOperandError - В выражении пропущен операнд
* TwoOperatorsInRowError - Два оператора стоят подряд
* UnbalancedParenthesesError - Операторы стоят подряд друг за другом
* ZeroDivError - Попытка деленяи на ноль
**Конвертер:**
* InvalidUnitError - Неизвестная величина
* IncompetibleUnitsError - Попытка конвертации несовместимых величин(mm -> f)
* InvalidValueError - Число написано с ошибкой
* TemperatureBelowAbsZero - Попытка подать на вход температуру ниже абсолютного нуля
**Сохранение истории проекта:**
* HistorySaveError - Не получилось сохранить историю

### Установка проекта
**Для всех:**
```bash
git clone https://github.com/Gelzy788/MAIPythonProject1.git
cd MAIPythonProject1
```

**Linux/MacOS**
```bash
python3 -m venv venv
source venv/bin/activate
pip install .
```
**Windows**
```bash
python -m venv venv
venv\Scripts\activate
pip install .
```