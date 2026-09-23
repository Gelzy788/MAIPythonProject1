from json import load, JSONDecodeError, dump

FILENAME = "history.json"   #NOTE: Мб стоит сделать отдельный файл config.py для таких констант
# NOTE Мб стоит поменять путь сохранения history.json

def add_calculation_to_history(example: str, result: float):
    history_data = read_history_file()
    new_data = {"type": "calculation",
                "example": example,
                "result": result}
    history_data.append(new_data)
    save_file(history_data)
    print("Данные добавлены")

def add_convertation_to_history(value: float, from_unit: str, to_unit: str, result: str):
    history_data = read_history_file()
    new_data = {"type": "convertation",
                "value": value,
                "from_unit": from_unit,
                "to_unit": to_unit,
                "result": result}
    history_data.append(new_data)
    save_file(history_data)
    print("Данные добавлены!")

def read_history_file():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            data = load(file)
    except (JSONDecodeError, FileNotFoundError) as err:
        data = []
    return data

def save_file(data: list):
    # TODO: Сделать обработку ошибок
    with open(FILENAME, "w", encoding="utf-8") as file:
        dump(data, file, indent=4)

