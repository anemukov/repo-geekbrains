#1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

input_num1 = (input("введите первое число "))
if not input_num1.isdigit():
    print("Вы ввели не число")
    exit()

input_num2 = (input("введите второе число "))
if not input_num2.isdigit():
    print("Вы ввели не число")
    exit()

input_num1 = int(input_num1)
input_num2 = int(input_num2)

def take_func(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("На ноль делить нельзя ")
        exit()
print(take_func(input_num1, input_num2))
