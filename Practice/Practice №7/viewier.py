from baza import *


def show():
    try:
        split_strings = (inf('info.csv'))
        name = input('Введите строку, с которой хотите книгу: ').strip()
        list = get_books(name, split_strings)
        out = (get_total(list))
        if len(out) == 0:
            print('Таких книг нет')
        else:
            print(out)
    except:
        print('какая-то ошибка')
