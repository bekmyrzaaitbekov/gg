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

#16
def battery_bars(percent):
    count = percent // 20
    return f"[{'#' * count}{'.' * (5 - count)}]"
#Для визуального отображения уровня заряда батареи в виде графического индикатора

#17
def reverse_words(s):
    return " ".join(s.split()[::-1])
#Нужна для изменения порядка слов в тексте

#18
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]
#Нужна для проверки слов или фраз на симметричность

#19
def stringy(size):
    return "".join("10"[i % 2] for i in range(size))
#Нужна для создания регулярных битовых последовательностей

#20
def square_or_square_root(arr):
    return [int(x**0.5) if int(x**0.5) ** 2 == x else x**2 for x in arr]
#Нужна для условного преобразования числовых последовательностей по математическому правилу

#21
def how_much_i_love_you(nb_petals):
    phrases = [
        "I love you",
        "a little",
        "a lot",
        "passionately",
        "madly",
        "not at all",
    ]
    return phrases[(nb_petals - 1) % 6]
#Нужна для создания циклических текстовых ответов на основе числового ввода

#22
def bin_to_decimal(inp):
    return int(inp, 2)
#Нужна для перевода двоичных представлений

#23
def hello(name=""):
    return f"Hello, {name.capitalize() or 'World'}!"
#Нужна для генерации персонализированных приветствий в чат-ботах

#24
def bmi(weight, height):
    b = weight / height**2
    if b <= 18.5:
        return "Underweight"
    elif b <= 25.0:
        return "Normal"
    elif b <= 30.0:
        return "Overweight"
    return "Obese"
#Для мониторинга и классификации состояния здоровья на основе индекса массы тела 

#25
def repeat_str(repeat, string):
    return string * repeat
#Нужна для форматирования текста, создания визуальных разделителей

#26
def points(games):
    return sum(
        3 if x > y else 1 if x == y else 0
        for x, y in (map(int, g.split(":")) for g in games)
    )
#Нужна для подсчета очков в спортивных соревнованиях на основе результатов матчей

#27
def is_divisible(n, x, y):
  return n % x == 0 and n % y == 0
#Нужна для проверки кратностей в алгоритмах

#28
def summation(num):
    return sum(range(1, num + 1))
#Нужна для вычисления суммы последовательных чисел

#29
def evil(n):
    return "It's Evil!" if bin(n).count("1") % 2 == 0 else "It's Odious!"
#Нужна для вычисления битовой четности

#30
def solution(a, b):
    return a + b + a if len(a) < len(b) else b + a + b
#Нужна для текстового форматирования
