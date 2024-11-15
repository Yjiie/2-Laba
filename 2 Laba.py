'''Лабораторная работа №2
Написать программу, решающую задачу из 1 лабораторной работы (в соответствии со своим вариантом) со следующими изменениями:
1.Входной файл является обыкновенным (т.е. нет требования на «бесконечность» файла);
2.Распознавание и обработку делать  через регулярные выражения;
3.В вариантах, где есть параметр (например К), допускается его заменить на любое число;
4.Все остальные требования соответствуют варианту задания лабораторной работы №1.
Вариант 14.
Четные двоичные числа, не превышающие 204810, у которых вторая справа цифра равна 0. Выводит на экран цифры числа, исключая нули. Вычисляется среднее число между минимальным и максимальным и выводится прописью.
'''
import re

def digit_to_text(digit):
    digit_dict = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    return digit_dict.get(digit, '')

valid_numbers = []

with open("text.txt", "r") as file:
    content = file.read()
    pattern = r'\b[01]+\b'
    binary_numbers = re.findall(pattern, content)

    for number in binary_numbers:
        if all(c in "01" for c in number):
            decimal_value = int(number, 2)
            if (
                    decimal_value <= 2048 and
                    decimal_value % 2 == 0 and
                    len(number) > 1 and number[-2] == '0'
            ):
                valid_numbers.append(decimal_value)
                print("Цифры числа, исключая нули:", " ".join(c for c in number if c != '0'))

if valid_numbers:
    min_value = min(valid_numbers)
    max_value = max(valid_numbers)
    avg_value = (min_value + max_value) // 2
    print("Среднее число прописью:", " ".join(digit_to_text(d) for d in str(avg_value)))
else:
    print("Не найдено подходящих чисел.")
