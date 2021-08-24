#1. Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

try:
    script_name, output_hour, rate_hour, award = argv
except ValueError:
    print("Вы ввели недостаточно данных")
    exit()

def staff_salary(output_hour, rate_our, award):
    return output_hour * rate_our + award

print("Выработка ", output_hour)
print("Ставка ", rate_hour)
print("Премия ", award)
print("Зарплата за месяц ", staff_salary(int(output_hour), int(rate_hour), int(award)))

