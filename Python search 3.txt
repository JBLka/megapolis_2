import csv

with open('rocket.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='@'))
    date = input()
    while date != "nlo":  # Пока мы не ввели "nlo"
        Is = True
        for i in reader:
            if i["date"] == date:  # Если дата совпадает
                print(f"Шифр: {i['code']} от: {i['rocketparts']} был получен {i['date']}")
                Is = False
                break
        if Is:  # Если дату не нашли
            print("такой сигнал еще не был получен")
        date = input()
