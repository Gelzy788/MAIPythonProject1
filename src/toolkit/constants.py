from json import load
from pathlib import Path
from re import VERBOSE, compile

# Путь к конфигурационному файлу для конвертации
UNITS_PATH = Path(__file__).parent / "units.json"

# Загрузка данных из файла units.json
with open(UNITS_PATH, "r", encoding="utf-8") as file:
    UNITS = load(file) # Все данные из файла

UNIT_GROUPS = {} # какой величине соответствует какая группа

for group, units in UNITS.items():
    for unit in units:
        UNIT_GROUPS[unit]= group



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

HISTORY_FILENAME = "history.json" # Название файла с историей вычислений
HISTORY_PATH = Path.cwd() / "logs" # Путь к файлу с историев вычислений

# Паттерн токенизации
TOKEN_PATTERN = compile(r"""
(?P<NUM>\d+(\.\d+)?) |
(?P<PLUS>\+) |
(?P<MINUS>-) |
(?P<MUL>\*) |
(?P<MOD>%) |
(?P<INTDIV>//) |
(?P<DIV>/) |
(?P<LPAREN>\() |
(?P<RPAREN>\)) |
(?P<OMISSION>\s+) |
(?P<UNKNOWN>.)
""", VERBOSE)

# Преобразование операций из названия группы в соответствующий символ
OPERATIONS = {
    "PLUS": "+",
    "MINUS": "-",
    "MUL": "*",
    "DIV": "/",
    "INTDIV": "//",
    "MOD": "%"
}

