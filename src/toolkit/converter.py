from toolkit.errors import TemperatureBelowAbsZero
from toolkit.units import UNITS, UNIT_GROUPS
from toolkit.converter_validation import validate_converter

def converter_manager(value: str, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    validate_converter(value, from_unit, to_unit)
    return convert(float(value), from_unit, to_unit)

def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    from_unit_data = UNITS["temperature"][from_unit]
    to_unit_data = UNITS["temperature"][to_unit]
    
    value_in_kelvin = (value - from_unit_data["zero_offset"]) / from_unit_data["coef"]
    result_value = value_in_kelvin * to_unit_data["coef"] + to_unit_data["zero_offset"]
    
    return result_value

def convert(value: float, from_unit: str, to_unit: str) -> float:
    group = UNIT_GROUPS[from_unit]
    
    if group == "temperature":
        if value < UNITS["temperature"][from_unit]["zero_offset"]:
            raise TemperatureBelowAbsZero
        else:
            return convert_temperature(value, from_unit, to_unit)
    else:
        coef = UNITS[group][from_unit] / UNITS[group][to_unit]
        return value / coef

if __name__ == "__main__":
    print(convert_len_and_weight(35, "Km", "m"))