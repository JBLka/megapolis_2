import csv


def paste_sort(file):  # Сортировка вставками по коду
    for i in range(1, len(file)):
        x = file[i]
        j = i
        while j > 0 and file[j - 1]["code"] > x["code"]:
            file[j] = file[j - 1]
            j -= 1
        file[j] = x
    return file


with open('rocket.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='@'))
    reader = paste_sort(reader)
    for i in reader:
        if "312" in i["code"]:  # Если 312 в коде
            print(f'{i["code"]} для {i["rocketparts"]}')

with open('errors.txt', "w", encoding='utf-8', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['date', 'code', 'rocketparts'],
                            delimiter='@')  # Сохраняем в файл errors.txt
    writer.writeheader()
    writer.writerows(reader)
