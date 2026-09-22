from json import load
from pathlib import Path

units_path = Path(__file__).parent / "units.json"

with open(units_path, "r", encoding="utf-8") as file:
    UNITS = load(file)

UNIT_GROUPS = {}

for group, units in UNITS.items():
    for unit in units.keys():
        UNIT_GROUPS[unit]= group
