from path import *


def show():
    flag = True
    while flag != False:
        print()
        print('0. Сменить рабочий каталог')
        print('1. Преобразовать PDF в Docx')
        print('2. Преобразовать Docx в PDF')
        print('3. Произвести сжатие изображений')
        print('4. Удалить группу файлов')
        print('5. Выход')
        print()
        choose = input('Выберите действие: ')
        print()
        if choose == '0':
            catalog = input('Введите абсолютный путь каталога: ')
            print(f"Текущий каталог: {change_catalog(catalog)}")
        elif choose == '1':
            chosen1()
        elif choose == '2':
            chosen2()
        elif choose == '3':
            chosen3()
        elif choose == '4':
            chosen4()
        elif choose == '5':
            flag = False
        else:
            print('Вы ошиблись, введите номер команды ещё раз')


if __name__ == "__main__":
    show()
