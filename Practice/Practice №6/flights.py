import re


def add_flight(a):
    datepat = re.compile("Рейс (\d+) (отправился|прибыл) (из|в) (\w+) в (\d+):(\d+):(\d+)")
    for m in datepat.finditer(a):
        newtext = datepat.sub(fix_date, a)
        return newtext


def fix_date(m):
    return f"[{m.group(5)}:{m.group(6)}:{m.group(7)}] - Поезд № {m.group(1)} {m.group(3)} {m.group(4)} "


def flights(file):
    info = [x[:-1] for x in file.readlines()]
    with open("new_flights.txt", mode="w", encoding="utf8") as new_flights:
        new_flights.write('')
    for string in info:
        new_format_fligh = (add_flight(string))
        if new_format_fligh != None:
            with open("new_flights.txt", mode="a", encoding="utf8") as new_flights:
                new_flights.write(f"{add_flight(string)}\n")


file = open('info_flights.txt', mode='r', encoding='utf-8')


