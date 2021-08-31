#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income = {"wage": 50000, "bonus": 10000}

class Position(Worker):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return print(f"ФИО сотрудника: {self.name} {self.surname}")

    def get_total_income(self):
        return print(f"Доход с учетом премии", self._income["wage"] + self._income["bonus"])

vasya = Position("Вася", "Пупкин")
vasya.get_full_name()
vasya.get_total_income()
