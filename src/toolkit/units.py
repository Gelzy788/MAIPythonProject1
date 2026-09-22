from json import load

with open("./src/toolkit/units.json", "r") as file:
    UNITS = load(file)

UNIT_GROUPS = {}

for group, units in UNITS.items():
    for unit in units.keys():
        UNIT_GROUPS[unit]= group
