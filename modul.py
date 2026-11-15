#1
def quarter_of(month):
    return (month + 2) // 3
#Нужна для определения квартала года по месяцу

#2
def whatday(num):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    return days.get(num, "Wrong, please enter a number between 1 and 7")
#Нужна для перевода числового обозначения дня недели в текстовое

#3
def swap_values(args: list) -> None:
    args[0], args[1] = args[1], args[0]
#Нужна для обмена местами значений переменных или элементов в массиве

#4
def parse_float(string):
    try:
        return float(string)
    except (ValueError, TypeError):
        return None
#Нужна для безопасного извлечения и конвертации чисел из текста

#5
def reverse_list(l):
    return l[::-1]
#Нужна для инвертирования порядка элементов в списке или массиве

#6
def set_alarm(employed, vacation):
    return employed and not vacation
#Нужна для настройки условий срабатывания будильника

#7
import sys


def total_bytes(obj):
    return sys.getsizeof(obj)
#Нужна для оптимизации памяти и анализа того, сколько весят различные структуры данных

#8
from functools import reduce
import operator


def logical_calc(array, op):
    ops = {
        "AND": operator.and_,
        "OR": operator.or_,
        "XOR": operator.xor,
    }
    return reduce(ops[op], array)
#Для вычисления общего логическог результата

#9
def neutralise(s1, s2):
    return "".join(
        c1 if c1 == c2 else "0" for c1, c2 in zip(s1, s2)
    )
#Для моделирования взаимодействия двух сигналов

#10
def hex_to_dec(s):
    return int(s, 16)
#Нужна для перевода шестнадцатеричных чис

#11
def powers_of_two(n):
    return [2**i for i in range(n + 1)]
#Нужна для создания последовательностей степеней двойки

#12
def expression_matter(a, b, c):
    return max(
        a + b + c,
        a * b * c,
        a * (b + c),
        (a + b) * c,
        a + b * c,
    )
#Нужна для поиска оптимального результата математических комбинаций

#13
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
#Нужна для классификации и распределения данных по возрастным диапазонам

#14
def double_char(s):
    return "".join(c * 2 for c in s)
#Нужна для текстовых трансформаций и спецэффектов

#15
def distinct(seq):
    return list(dict.fromkeys(seq))
#Нужна для очистки списков от повторяющихся данных