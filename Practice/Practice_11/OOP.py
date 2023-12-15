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

'''class SuperStr(str):
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
'''


# 4

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {'Linal': [5], 'C++': [10]}
        self.average_grades = self.grades.values()

    def add_courses(self, course_name):
        if not course_name in self.finished_courses:
            self.finished_courses.append(course_name)
            if course_name in self.courses_in_progress:
                self.courses_in_progress.pop(course_name)
        else:
            print(f'Студент {self.name + self.surname} уже закончил курс {course_name}')

    def add_courses_in_progress(self, course_name):
        if not course_name in self.courses_in_progress:
            self.courses_in_progress.append(course_name)
        else:
            print(f'Студент {self.name + self.surname} уже закончил курс {course_name}')

    def rate_lecturer(self, lecturer, course, grade):
        if course in lecturer.courses_attached:
            if isinstance(grade, int) and grade >= 1 and grade <= 10:
                if course in lecturer.lecturer_grades:
                    lecturer.lecturer_grades[course].append(grade)
                else:
                    lecturer.lecturer_grades[course] = grade
            else:
                return ('Оценка должна быть целым числом от 1 до 10')

    def get_average_grades(self, student):
        grades = self.grades
        return (sum(grades.values())) / len(grades)

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за домашние задания: {self.average_grades} \n" \
               f"Курсы в процессе изучения: {self.courses_in_progress} \n" \
               f"Завершенные курсы: {self.finished_courses}"

    def __int__(self):
        return f"Кол-во курсов завершённых и в прогрессе: {len(self.courses_in_progress) + len(self.finished_courses)}"

    def __bool__(self):
        pass


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __int__(self):
        return f"Кол-во прилагаемых предметов: {len(self.courses_attached)}"

    def add_attached_courses(self, course):
        self.courses_attached.append(course)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        # Mentor.__init__(self, self.name, self.surname)
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: "


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(grade, int) and grade >= 1 and grade <= 10:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            print('Оценка должна быть целым числом от 1 до 10')

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} "


Loshped = Student('Seryoga', 'Oreshkin', 'Male')
Angry = Reviewer('Jack', 'Fresko')
Bobbinson = Lecturer('Oleg', 'Tinkoff')
Angry.rate_student(Loshped, 'Linal', 5)
Angry.add_attached_courses('Linal')
Bobbinson.add_attached_courses('Linal')
Loshped.rate_lecturer(Bobbinson, 'Linal', 1)
print(Bobbinson.lecturer_grades)
print(str(Loshped))
print(Loshped.grades)
