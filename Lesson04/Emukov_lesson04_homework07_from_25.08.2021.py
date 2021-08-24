#7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

#x = 1
#def fact_generation():
    #for el in [2, 5, 10]:
        #yield el

#print(fact_generation())

#for x in fact_generation():
    #print(x)

from itertools import count
from math import factorial


def fact_generator():
    for i in count(1):
        yield factorial(i)

generator = fact_generator()
x = 0
for k in generator:
    if x < 5:
        print(k)
        x += 1
    else:
        break