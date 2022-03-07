class Veichle:
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Car(Veichle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print('Beep Beep')


class Truck(Car):
    def __init__(self, price, gas, color, speed, tires):
        super().__init__(price, gas, color, speed)
        self.speed = speed
        self.tires = tires

    def beep(self):
        print('Honk Honk')


volvo = Veichle(10.000, 100, 'green')
print(volvo.gas)

truck1 = Truck(100.000, 50, 'blue and red', 40, 10)

print(truck1.speed)
truck1.beep()
