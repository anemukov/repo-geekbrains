#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:

    def __init__(self, date_info):
        self.date_info = str(date_info)


    @classmethod
    def show_date(cls, date_info):
        ind_date = []

        for x in date_info.split():
            if x != '-': ind_date.append(x)

        return f"{int(ind_date[0]):02}.{int(ind_date[1]):02}.{int(ind_date[2])}"

    @staticmethod
    def validation(day, month, year):
        if 31 >= day > 0:
            if 12 >= month > 0:
                if 2022 > year > 0:
                    return f"{day:02}.{month:02}.{year}"

                else:
                    print("Вы ввели неправильный год")
            else:
                print("Вы ввели неправильный месяц")
        else:
            print("Вы ввели неправильный день")


print(Date.show_date("4 - 9 - 2021"))
print(Date.validation(15, 2, 2021))
print(Date.validation(32, 12, 2021))
print(Date.validation(4, 15, 2021))
print(Date.validation(4, 12, 2023))
