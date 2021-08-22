#2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

first_name = input("Введите Ваше имя ")
last_name = input("Введите Вашу фамилию ")
birthday = input("Введите год рождения ")
place_living = input("Введите город проживания ")
email = input("Введите Ваш email ")
phone = input("Введите Ваш номер телефона ")

def user_info(*args):
    return args

res1, res2, res3, res4, res5, res6 = \
    user_info(first_name, last_name, birthday,
              place_living, email, phone)

print(res1, res2, res3, res4, res5, res6)
