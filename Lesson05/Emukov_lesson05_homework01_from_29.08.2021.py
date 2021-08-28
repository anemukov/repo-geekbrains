#1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("501.txt", "w", encoding="UTF-8") as input_list:
    input_users = input("Введите данные через пробел ").split()

    for line in input_users:
        input_list.write(line + "\n")
