# TODO импортировать необходимые молули
import json
import csv
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, encoding="utf-8") as f:
        data_list = [data for data in csv.DictReader(f)] # создаем список словарей из cvs файла
    with open(OUTPUT_FILENAME,"w", encoding="utf-8") as f:
       json.dump(data_list, f, indent = 4,)

    # TODO считать содержимое csv файла

     # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME,) as output_f:
        for line in output_f:
            print(line, end="")




