from json import load
from pathlib import Path
from re import VERBOSE, compile

UNITS_PATH = Path(__file__).parent / "units.json"

with open(UNITS_PATH, "r", encoding="utf-8") as file:
    UNITS = load(file)

UNIT_GROUPS = {}

for group, units in UNITS.items():
    for unit in units.keys():
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

HISTORY_FILENAME = "history.json"
HISTORY_PATH = Path(__file__).parent.parent.parent / "logs"
HISTORY_PATH.mkdir(exist_ok=True)

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

OPERATIONS = {
    "PLUS": "+",
    "MINUS": "-",
    "MUL": "*",
    "DIV": "/",
    "INTDIV": "//",
    "MOD": "%"
}

