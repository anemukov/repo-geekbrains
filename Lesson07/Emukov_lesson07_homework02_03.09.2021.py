#2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

class Clothes:

    def __init__(self, v, h):
        self.v = v
        self.h = h

    def calc_coat(self):
        #self.v = v
        return self.v/6.5 + 0.5

    def calc_suit(self):
        #self.h = h
        return 2*self.h + 0.3

    @property
    def full_calc(self):
        return f"Общий расход ткани {self.calc_coat() + self.calc_suit()}"

class Coat(Clothes):

    def __init__(self, v, h):
        super().__init__(v, h)
        self.coat_calc = self.calc_coat()

    def __str__(self):
        return self.coat_calc

class Suit(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.suit_calc = self.calc_suit()

    def __str__(self):
        return self.suit_calc

a = Clothes(10, 5)
print(a.calc_coat())
print(a.calc_suit())
print(a.full_calc)
b = Coat(15, 3)
c = Suit(20, 4)
print(b.calc_coat(), "и", b.calc_suit())
print(b.full_calc)
print(c.calc_coat(), "и", c.calc_suit())
print(c.full_calc)
