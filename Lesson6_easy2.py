class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stopping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))


class TownCar(Car):
    pass


class SportCar(Car):
    def __init__(self, speed, color, name, has_turbo=True):
        super().__init__(speed, color, name)
        self.has_turbo = has_turbo


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


sportCar = SportCar(220, 'black', 'sport')
townCar = TownCar(160, 'yellow', 'town')
workCar = WorkCar(100, 'red', 'work')
policeCar = PoliceCar(200, 'white', 'police')


print(policeCar.is_police)

for i in townCar:
 print(i)
