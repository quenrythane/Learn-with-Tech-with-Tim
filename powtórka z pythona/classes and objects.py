class Dog(object):
    def __init__(self, name, age):  # self oznacza tutaj tim
        self.name = name  # to oznacza, że tim.name =  name
        # (a name to jest to co u góy wpisaliśmy)
        self.age = age

    def speak(self):
        print('hi! I am', self.name)

    def change_age(self, age):
        self.age = age

    def add_weight(self, xd):
        self.weight = xd

    def talk(self):
        print('Bark!')


tim = Dog('Tim', 26)
tim.speak()
print(tim)
tim.add_weight(20)
print(tim.weight)
print('name:', tim.name, 'age:', tim.age, 'weight:', tim.weight)
print('\n\n')


# part 2
class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    # nadpisuje talk zeby kot miauczał a nie szczekał
    def talk(self):
        print('Meow!')


tom = Cat('Tom', 15, 'grey')
tom.speak()
tom.talk()
tim.talk()