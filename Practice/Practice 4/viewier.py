from save import *


def show():
    try:
        name = input(f"Введите имя файла: ").strip()
        words = read_file(f"{name}.txt")
        save_file('count.txt', words)
    except FileNotFoundError:
        print("Такого файла нет! Перезапустите программу и попробуйте ещё раз. ")

if __name__ == "__main__":
    show()
