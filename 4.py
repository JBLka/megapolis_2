import csv


def paste_sort(file):  # Сортировка вставками по дате
    for i in range(1, len(file)):
        x = file[i]
        j = i
        while j > 0 and file[j - 1]["date"] > x["date"]:
            file[j] = file[j - 1]
            j -= 1
        file[j] = x
    return file


with open('rocket.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='@'))
    reader = paste_sort(reader)
    for i in reader:
        dates = sorted([j["date"] for j in reader if
                        j["rocketparts"] == i["rocketparts"]])  # Сохраняем все даты, связанные с деталью
        i["queue"] = str(dates.index(i["date"]) + 1) + i["code"] + i["rocketparts"][0]  # Генерируем код

with open('rocket_code.csv', "w", encoding='utf-8', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['date', 'code', 'rocketparts', "queue"],
                            delimiter='@')  # Сохраняем в файл rocket_code.csv
    writer.writeheader()
    writer.writerows(reader)
