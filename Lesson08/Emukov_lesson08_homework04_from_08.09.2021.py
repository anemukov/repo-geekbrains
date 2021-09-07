#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class StockEquipment:
    pass

class OfficeEquipment:
    type_equipment: str
    name_equipment: str
    articul: str

class Printer(OfficeEquipment):
    color_printing: bool

class Scaner(OfficeEquipment):
    dpi = int

class Copier(OfficeEquipment):
    color_copier = bool
