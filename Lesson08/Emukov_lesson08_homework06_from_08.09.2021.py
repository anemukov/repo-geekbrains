#6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
#Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.

class AllErrors(Exception):

    def __init__(self, param):
        self.param = param

class StockEquipment:

    def __init__(self):
        self._dict = {}
        self._dict1 = {}

    def add_to_stock(self, office_equipment):
        if self._dict.setdefault(office_equipment.group_name(), []).append(office_equipment):
            raise AllErrors("Такой техники нет")
        else:
                self._dict.setdefault(office_equipment.group_name(), []).append(office_equipment)

    def extract_from_stock(self, name_equipment):
        if not self._dict[name_equipment]:
                 raise AllErrors("Такой техники нет")
        else:
            self._dict.setdefault(name_equipment).pop(0)
            self._dict1.setdefault(name_equipment, []).append(name_equipment)


class OfficeEquipment:
    type_equipment: str
    name_equipment: str
    articul: str

    def __init__(self, name_equipment, articul):
        self.name_equipment = name_equipment
        self.articul = articul
        self.group = self.__class__.__name__

    def group_name(self):
        return f"{self.group}"

    def __repr__(self):
        return f"Данные по технике: Наименование: {self.name_equipment}, Артикул: {self.articul}"

class Printer(OfficeEquipment):
    color_printing: bool

    def __init__(self, name_equipment, articul, color_printing):
        super().__init__(name_equipment, articul)
        self.color_printing = color_printing

    def __repr__(self):
        return f"Модель: {self.name_equipment}, Артикул: {self.articul}, Цветной: {self.color_printing}"


class Scaner(OfficeEquipment):
    dpi: int

    def __init__(self, name_equipment, articul, dpi):
        super().__init__(name_equipment, articul)
        self.dpi = dpi

        if not self.dpi.isdigit():
            raise AllErrors("Вы вввели не число")

    def __repr__(self):
        return f"Модель: {self.name_equipment}, Артикул: {self.articul}, Разрешение: {self.dpi}"

class Copier(OfficeEquipment):
    color_copier = bool

    def __init__(self, name_equipment, articul, color_copier):
        super().__init__(name_equipment, articul)
        self.color_printing = color_copier

    def __repr__(self):
        return f"Модель: {self.name_equipment}, Артикул: {self.articul}, Цветной: {self.color_printing}"

stock = StockEquipment()

#print(OfficeEquipment("Printer", "HP 5037", "123467RU"))
#print(Printer("Brother 1287W", "B-RU1508", True))
#print(Scaner("HP 2050", "8095645RU", 1200))
#print(Copier("Brother 8090RW", "B-RU884532", False))
printer = Printer("Brother 1287W", "B-RU1508", True)
stock.add_to_stock(printer)
scaner = Scaner("HP 2050", "8095645RU", "fss")
stock.add_to_stock(scaner)
copier = Copier("Brother 8090RW", "B-RU884532", False)
stock.add_to_stock(copier)
printer = Printer("Oliver 4315", "5839456RU", False)
stock.add_to_stock(printer)
print(stock._dict, '\n')
#stock.extract_from_stock("Computer")
stock.extract_from_stock("Printer")
stock.extract_from_stock("Scaner")
print(stock._dict, "\n")
print(stock._dict1)