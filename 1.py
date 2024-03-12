import csv

with open("rocket.txt", encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='@'))
    rocketparts = {}
    for i in reader:
        if i["rocketparts"] not in rocketparts.keys():  # Добавляем деталь в словарь, если её там нет
            rocketparts[i["rocketparts"]] = 1
        else:
            rocketparts[i["rocketparts"]] += 1  # Увеличиваем значение детали, если он есть
    reader = []
    for i in rocketparts:
        reader.append({"rocketPart": i, "countCode": rocketparts[i]})

with open("rocket_part.txt", "w", encoding='utf-8', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["rocketPart", "countCode"], delimiter='@')
    writer.writeheader()
    writer.writerows(reader)
    print(rocketparts[input()])  # Выводим количество деталей, название которой мы ввели
