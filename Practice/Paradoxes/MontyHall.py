import random
from random import *


def monty(n):
    count_second_choice_win = 0  # подсчёт побед, когда согласился изменить свой выбор
    count_first_choice_win = 0
    count_try = 0
    for i in range(n):
        priz = randint(1, 3)  # приз здесь
        print(f"Приз в двери номер {priz}, но участник об этом не знает.")
        computer = randint(1, 3)  # начальный выбор игрока
        print(f"Я выбираю дверь под номером {computer}.")
        print(f"Игрок выбрал дверь под номером {computer}. Что-ж, давайте сначала посмотрим на одну из пустых дверей!")
        not_here = [int(x) for x in range(1, 4) if x != priz and x != computer]  # приз ни в одной из этих дверей
        lose_door = choice(not_here)  # дверь, которую мы будем открывать, где нет приза
        print(f"Откройте дверь номер {lose_door} !")
        print(
            f"Итак, участник, желаете ли вы изменить свой выбор: поменять дверь номер {computer} на дверь номер {6 - computer - lose_door}?")
        second_choice_computer = choice(['да', 'нет'])
        if second_choice_computer == 'да':
            print(f"Я решил, что приз в двери номер {6 - computer - lose_door} и я меняю свой выбор")
            print(f"Откройте дверь номер {6 - computer - lose_door}!")
            if 6 - computer - lose_door == priz:
                print(f"Поздравляем! Вы выбрали дверь номер {6 - computer - lose_door} и не ошиблись, приз ваш!")
                count_second_choice_win += 1
                count_try += 1
            else:
                print(
                    f"Вы изменили свой выбор и оказались не правы! Увы, сегодня не ваш день, в двери номер {6 - computer - lose_door} приза нет(")
                count_try += 1
        else:
            print(f"Я уверен, что приз в двери номер {computer} и не буду менять выбор")
            print(f"Откройте дверь номер {computer}!")
            if computer == priz:
                print(f"Поздравляем! Вы выбрали дверь номер {computer} и не ошиблись, приз ваш!")
                count_first_choice_win += 1
                count_try += 1
            else:
                print(
                    f"Вы остались при своём мнении и оказались не правы! Увы, сегодня не ваш день, в двери номер {computer} приза нет")
                count_try += 1
        print(' ')
    return count_try, count_first_choice_win, count_second_choice_win


print(monty(10))
