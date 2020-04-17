#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} поехали'

    def stop(self):
        return f'{self.name} стоп'

    def turn_right(self):
        return f'{self.name} повернули направо'

    def turn_left(self):
        return f'{self.name} повернули налево'

    def show_speed(self):
        return f'Текущая скорость {self.name}  {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость для городского автомобиля {self.name}  {self.speed}')

        if self.speed > 60:
            return f'Сорость {self.name} превышает допустимую для городского автомобиля '
        else:
            return f'Скорость {self.name} допустима для городского автомобиля'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость для грузового автомобиля {self.name}  {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышает допустимую для грузового автомобиля'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский автомобиль'
        else:
            return f'{self.name} не полицейский автомобиль'


audi = SportCar(100, 'красный', 'Audi', False)
oka = TownCar(30, 'Белый', 'Ока', False)
lada = WorkCar(70, 'Вишневая', 'Lada', True)
ford = PoliceCar(110, 'Зеленый',  'Ford', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, чем {audi.stop()}')
print(f'{lada.go()} со скоростью {lada.show_speed()}')
print(f'{lada.name}  {lada.color}')
print(f'Этот {audi.name} полицейский автомобиль? {audi.is_police}')
print(f'Этот {lada.name}  полицейский автомобиль? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())