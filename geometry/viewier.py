'''if __name__ == "__main__":
    from .square import *
    from .perimetr import *

    show()
else:
    from .square import *
    from .perimetr import *'''


def show():
    print('Выберите функцию: ')
    print("1.Площадь квадрата \
          \n2.Площадь прямоугольника\
            \n3. Площадь треугольника\
           \n4.Периметр любой геометрической фигуры")
    c = (input())
    if c == '1':
        print(f"Площадь квадрата: {sq_sq(float(input('Введите длину стороны а: ')))}")
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
