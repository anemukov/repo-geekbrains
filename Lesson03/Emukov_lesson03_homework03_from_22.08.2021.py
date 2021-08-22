#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

num_1 = input("Введите первое число ")
if not num_1.isdigit():
    print("Вы ввели не число")
    exit()
num_2 = input("Введите второе число ")
if not num_2.isdigit():
    print("Вы ввели не число")
    exit()
num_3 = input("Введите третье число ")
if not num_3.isdigit():
    print("Вы ввели не число")
    exit()
num_1 = int(num_1)
num_2 = int(num_2)
num_3 = int(num_3)

def my_func(a, b, c):
    if b > c < a:
        return a + b
    elif a > b < c:
        return a + c
    else:
        return b + c

numbers = my_func(num_1, num_2, num_3)

print(numbers)
