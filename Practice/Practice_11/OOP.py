# 1
'''class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def turn_on_car(self):
        return 'Автомобиль заведён'

    def turn_off_car(self):
        return 'Автомобиль заглушен'

    def type_of_car(self, type):
        self.type = type
        return self.type

    def year_of_car(self, year):
        self.year = year
        return self.year

    def color_of_car(self, color):
        self.color = color
        return self.color


Turbo = Car('Жёлтая', 'Легковая', '1974')
print('Цвет - ', Turbo.color)
print('Тип - ', Turbo.type)
print('Год выпуска - ', Turbo.year)

Turbo.type_of_car('лёгкая')
print('Тип - ', Turbo.type)
Turbo.color_of_car('yellow')
print('Цвет - ', Turbo.color)
Turbo.year_of_car('2005')
print('Год выпуска - ', Turbo.year)
print(Car.turn_on_car(Turbo))
print(Car.turn_off_car(Turbo))'''

# 2
'''import math

class Sphere:
    def __init__(self, r, x=0, y=0, z=0):
        self.r = r
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def get_volume(self):
        return (4 / 3) * (math.pi) * (self.r) ** 3

    def get_square(self):
        return 4 * math.pi * ((self.r) ** 2)

    def get_radius(self):
        return float(self.r)

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if (x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2 <= (self.r) ** 2:
            return True
        else:
            return False


s0 = Sphere(0.5)
print(s0.get_center())
print(s0.get_volume())
print(s0.is_point_inside(0, -1.5, 0))
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0))
print(s0.get_radius())'''


# 3

class SuperStr(str):
    def __init__(self, stroka):
        self.stroka = stroka

    def is_repeatance(self, s):
        if isinstance(s, str) == False:
            return False
        elif len([x for x in self.stroka.split(s) if len(x) > 0]) == 0:
            return True
        else:
            return False

    def is_palindrom(self):
        if self.stroka == self.stroka[::-1]:
            return True
        else:
            return False


s = SuperStr("123123123123")
print(s.is_repeatance("123"))  # True
print(s.is_repeatance("123123"))  # True
print(s.is_repeatance("123123123123"))  # True
print(s.is_repeatance("12312"))  # False
print(s.is_repeatance(123))  # False
print(s.is_palindrom())  # False
print(s * 2)  # 123123123123 (строка)
print(int(s) * 2)  # 123123123123 (целое число)
print(s + "qwe")  # 123123123123qwe
p = SuperStr("123_321")
print(p.is_palindrom())  # True
