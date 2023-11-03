'''if __name__ == "__main__":
    from .square import *
    from .perimetr import *

    show()
else:
    from .square import *
    from .perimetr import *'''


def show():
    print("Парадокс Монти Холла: введите кол-во экспериментов")
    c = (input())
    if c == '1':
        print(f"Побед, % побед с первого хода,  % побед со 2-го хода соответственно: {monty(10000)}")
    elif c == '2':
        print(
            f"Площадь прямоугольника: {sq_pr(float(input('Введите длину стороны а: ')), float(input('Введите длину стороны b: '))),}")
    elif c == '3':
        print(
            f"Площадь треугольника: {sq_te(float(input('Введите длину стороны а: ')), float(input('Введите длину высоты h: ')))}")
    elif c == '4':
        print(
            f"Площадь любой геометрической фигуры: {perimetr(*[float(i) for i in input('введите длины через запятую: ')])}")


if __name__ == "__main__":
    from .square import *
    from .perimetr import *

    show()
else:
    from .square import *
    from .perimetr import *

'''if __name__ == "__main__":
    show()'''
