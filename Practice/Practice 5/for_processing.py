import os


def processing():
    try:
        name = input('Введите имя текстового файла, из которого хотите импортировать данные: ').strip()
        f = open(f"{name}.txt")
        n = int(f.readline())
        a = [int(f.readline()) for x in range(n)]
        f.close()
        return a
        '''if not os.path.exists(f"{name}.txt"):
                flag = False
                while flag != True:
                    name = input('Такого файла нет, вы ошибились, попробуйте ещё раз: ').strip()
                    if os.path.exists(f"{name}.txt"):
                        flag = True'''
    except FileNotFoundError:
        print("Такого файла нет! Введите название файла ещё раз! ")
        return processing()
    except ValueError:
        print('В файле какая-то хуйня. Перепроверь')


# print(processing())
