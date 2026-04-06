# TODO решите задачу
import json
INPUT_FILE = "input.json"

def task() -> float:
    with open(INPUT_FILE) as f:
        json_data = json.load(f)
        list_values = [item["weight"] * item["score"]  for item in json_data] # произведение "score" * "weight" в каждом словаре
        return round(sum(list_values),3) # сумма этих произведений с округлением до 3 знаков после запятой

print(task())
