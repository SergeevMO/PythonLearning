'''
Во втором Python были классы старого стиля class Car(object):
'''

class Car:
    body = 'regular'
    # position = [0, 0, 0]
    max_speed = 200 # km/h
    state = 'stopped'
    speed = 0 # km/h

# инициализатор объекта записывает переданные параметры в словарь объекта
    def __init__(self, color, gas_tank):
        self.color = color
        self.gas_tank = gas_tank # l
        self.position = [0, 0, 0]
    
    def __lt__(self, other):
        return self.speed < other.speed

# интерфейс:
    def start(self):
        print('Wroom!')
        print('inside class: ', self)
        self.state = 'started'
    
    def fill_gas_tank(self, gas):
        self.gas_tank += gas

    def accelerate(self, v):
        if self.speed + v > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += v
    
    def go(self, h):
        self.position += self.speed * h
        self.gas_tank -= 10 * h
    
    def brake(self):
        self.speed = 0

    def stop(self):
        self.state = 'stopped'

class Expensive: 
    price = 100000000000000000000 # $

    def brake(self):
        self.speed = 100


class Cabrio(Car, Expensive): # множественное наследование
    roof_color = 'black'
    roof_state = 'убрана'
    max_speed = 250 # переопределение атрибута

    def __init__(self, color, gas_tank):
        print('Внутренний инициализатор')
        super().__init__(color, gas_tank) # вызов методов родительского класса


    def fold_roof(self):
        self.roof_state = 'folded'

    def unfold_roof(self):
        self.roof_state = 'unfolded'

    def start(self):             # переопределение метода
        print('Wroom, wroom!')   # добавление нового свойства
        super().start()          # добавление всего тела метода от родительского класса 

cabrio_0 = Cabrio('red', 50)
cabrio_0.fill_gas_tank(10)
print(cabrio_0.position)
cabrio_0.start()
cabrio_0.accelerate(270)
print(cabrio_0.speed)
cabrio_0.start()

car_0 = Car('black', 20)
# car_0.roof_color           - так нельзя

cabrio_0.brake()
print(cabrio_0.speed) # если имена методов совпадают, то используется метод из первого класса


cabrio_0 = Cabrio('red', 50)
cabrio_1 = Cabrio('red', 50)
cabrio_0.accelerate(100)
cabrio_1.accelerate(120)

# оператор сравнения не поддерживается пока его не переопределишь
print(cabrio_0 > cabrio_1)
# операторы < и > взаимозаменяемы, поэтому можно переопределить только один из них

print(Cabrio.mro()) # описывает иерархию наследования классов