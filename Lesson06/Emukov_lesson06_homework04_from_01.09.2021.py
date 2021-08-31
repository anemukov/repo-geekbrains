#4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, manevr):
        print(f"Машина повернула {manevr}")

    def show_speed(self, speed):
        self.speed = speed

class TownCar(Car):
    color = "белый"
    name = "Мазда"
    is_police = False
    speed = 70

    def touncar_method(self):
        print("Это городская машина")

    def show_speed(self, speed):
        if speed > 60:
            print("Скорость городской машины превышена")

class SportCar(Car):
    color = "Желтый"
    name = "Ламборгини"
    is_police = False
    speed = 150

    def sportcar_method(self):
        print("Это спортивная машина")

class WorkCar(Car):
    color = "синий"
    name = "Пежо"
    is_police = False
    speed = 50

    def workcar_method(self):
        print("Это рабочая машина")

    def show_speed(self, speed):
        if speed > 40:
            print("Скорость рабочей машины превышена")


class PoliceCar(Car):
    color = "белый"
    name = "Форд"
    is_police = True
    speed = 100

    def police_method(self):
        print("Это полицейская машина")

tcar = TownCar()
scar = SportCar()
wcar = WorkCar()
pcar = PoliceCar()
print(tcar.__dict__)
print(scar.__dict__)
print(wcar.__dict__)
print(pcar.__dict__)
tcar.show_speed(70)
wcar.show_speed(50)
tcar.go()
scar.turn("налево")
pcar.speed = 200
tcar.color = "Черный"
scar.is_police = False
wcar.name = "Renault"
pcar.police_method()
print(tcar.__dict__)
print(scar.__dict__)
print(wcar.__dict__)
print(pcar.__dict__)
