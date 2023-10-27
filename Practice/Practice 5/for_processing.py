import os


def processing():
    name = input('Введите имя текстового файла, из которого хотите импортировать данные: ').strip()
    if not os.path.exists(f"{name}.txt"):
        flag = False
        while flag != True:
            name = input('Такого файла нет, вы ошибились, попробуйте ещё раз: ').strip()
            if os.path.exists(f"{name}.txt"):
                flag = True
    f = open(f"{name}.txt")
    n = int(f.readline())
    a = [int(x) for x in f.readlines()]
    f.close()
    return a


print(processing())
