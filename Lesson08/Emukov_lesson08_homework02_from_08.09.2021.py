#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyException(Exception):
    def __init__(self, param):
        self.param = param

try:
    num_1 = int(input("Введите числитель "))
    num_2 = int(input("Введите знаменатель "))
    if num_2 == 0:
        raise MyException("Вы ввели ноль в знаменателе, на ноль делить нельзя")
    else:
        print(num_1 / num_2)
except ValueError:
    print("Вы ввели не число")
except MyException as error:
    print(error)



