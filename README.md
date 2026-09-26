# Программирование на Python. Лабораторная работа №1

> Консольный калькулятор и  конвертер величин

---

## ✨ Возможности

### 🧮 Калькулятор
- Операции: `+`, `-`, `*`, `/`, `//`, `%`
- Скобки и учёт приоритетов операций
- Унарные операторы
  > ⚠️ При использовании калькулятора если у вас стоит в начале выражени минус надо поставить перед ковычками "--"

### 🔄 Конвертер
- **Длина:** `mm`, `cm`, `m`, `km`
- **Масса:** `g`, `kg`
- **Температура:** `c` (Цельсий), `f` (Фаренгейт), `k` (Кельвин)
  > ⚠️ Температура не может быть ниже абсолютного нуля

### 💾 История операций
- Успешные операции сохраняются в `logs/history.json`

---

## 📁 Структура проекта

src/toolkit/
├── init.py
├── main.py                  # Точка входа программы
├── calc_validation.py       # Валидация калькулятора
├── calculator.py            # Перевод в RPN и вычисление
├── constants.py             # Служебные константы
├── converter_validation.py  # Валидация конвертера
├── converter.py             # Функционал конвертера
├── errors.py                # Собственные исключения
├── history_saver.py         # Сохранение истории в logs/history.json
├── tokenizer.py             # Токенизатор выражений
└── units.json               # Коэффициенты конвертации

---

## 🚀 Команды запуска

```bash
python -m toolkit calc "EXPRESSION"
python -m toolkit convert VALUE --from UNIT --to UNIT
python -m toolkit --help
```

---

## 🚨 Возможные ошибки

### 🧮 Калькулятор
| Ошибка | Описание |
|---|---|
| `FloatSpecialDivError` | Спец. деление (`//`, `%`) с дробными числами |
| `EmptyExpressionError` | Передано пустое выражение |
| `InvalidSymbolError` | Неизвестный символ в выражении |
| `MissingOperatorError` | Пропущен оператор |
| `MissingOperandError` | Пропущен операнд |
| `TwoOperatorsInRowError` | Два оператора подряд |
| `UnbalancedParenthesesError` | Несбалансированные скобки |
| `ZeroDivError` | Деление на ноль |

### 🔄 Конвертер
| Ошибка | Описание |
|---|---|
| `InvalidUnitError` | Неизвестная единица измерения |
| `IncompetibleUnitsError` | Несовместимые величины (например, `mm → f`) |
| `InvalidValueError` | Некорректно записано число |
| `TemperatureBelowAbsZero` | Температура ниже абсолютного нуля |

### 💾 История
| Ошибка | Описание |
|---|---|
| `HistorySaveError` | Не удалось сохранить историю |

---

## 🛠 Установка

### Клонирование
bash
git clone https://github.com/Gelzy788/MAIPythonProject1.git
cd MAIPythonProject1

### 🐧 Linux / 🍎 macOS
```bash
python3 -m venv venv
source venv/bin/activate
pip install .
```

### 🪟 Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install .
```