import csv


def paste_sort(file):  # Сортировка вставками по коду
    for i in range(1, len(file)):
        x = file[i]
        j = i
        while j > 0 and file[j - 1]["countCode"] > x["countCode"]:
            file[j] = file[j - 1]
            j -= 1
        file[j] = x
    return file[::-1][:10]


with open("rocket.txt", encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='@'))
    rocketparts = {}
    for i in reader:
        if i["rocketparts"] not in rocketparts.keys():  # Добавляем деталь в словарь, если её там нет
            rocketparts[i["rocketparts"]] = 1
        else:
            rocketparts[i["rocketparts"]] += 1  # Увеличиваем значение детали, если она есть
    reader = []
    for i in rocketparts:
        reader.append({"rocketPart": i, "countCode": rocketparts[i]})
    reader = paste_sort(reader)

with open("top_10.txt", "w", encoding='utf-8', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["rocketPart", "countCode"], delimiter='@')
    writer.writeheader()
    writer.writerows(reader)
    # Я выполнил задачу так, как я её понял
