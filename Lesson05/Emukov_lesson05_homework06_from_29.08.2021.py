#6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

#dict_objects = {}

import re

def calculate_hours(calc_line: str):
    amount_hours = re.sub(r"\D", " ", calc_line)
    calc_hours = 0
    for hour in amount_hours.split():
        calc_hours += int(hour)
    return calc_hours


dict_objects = {}
with open("506.txt", encoding='utf-8') as read_objects:
    for line in read_objects.readlines():
        object_line = line.split(': ')
        dict_objects[object_line[0]] = calculate_hours(object_line[1])

print(f"Словарь предметов: {dict_objects}")