#6. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def draw(self):
        print("Запуск отрисовки")

class Pen:
    title = "Pen"

    def draw(self):
        print("Это класс Pen")

class Pencil:
    title = "Pencil"

    def draw(self):
        print("Это класс Pencil")


class Handle:
    title = "Handle"

    def draw(self):
        print("Это класс Handle")

basic = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
basic.draw()
pen.draw()
pencil.draw()
handle.draw()