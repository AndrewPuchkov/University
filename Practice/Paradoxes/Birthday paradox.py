import random

from random import *


def birthday(count_groups, count_tipov_in_group):
    true_statement = 0  # верно ли, что есть хотя бы одна пара, подсчёт таких групп
    for l in range(count_groups):  # создаём 10000 групп
        k = 0  # кол-во совпадений в начале 0
        birthdays = [[randint(1, 28), randint(1, 12)] for x in range(count_tipov_in_group)]  # группа создается
        # flag = False
        for i in range(count_tipov_in_group - 1):  # берём одного человека из пары
            for j in range(i + 1, count_tipov_in_group):  # берём второго человека из пары
                if birthdays[i] == birthdays[j]:  # если равны, то кайф увеличивается на 1
                    k += 1
                    '''true_statement += 1 
                    flag = True # здесь я пытался избежать лишних проверок и сделать прогу поэффективнее, ведь если есть хотя бы одна пара, то можно выходить
                    # print(birthdays)
                    break
            if flag == True:
                break'''
        if k > 0:  # после подсчёта свопадений в группе если хотя бы одно свопадение есть, то утверждение верно
            true_statement += 1
    return f"{int((true_statement / count_groups) * 100)} %"


print(f"Парадокс дней рождения в группе из 23 человек среди 10000 экспериментов: {birthday(10000, 23)}")
print(f"Парадокс дней рождения в группе из 60 человек среди 10000 экспериментов: {birthday(10000, 60)}")
