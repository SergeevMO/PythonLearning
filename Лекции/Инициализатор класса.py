class Car():
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


# при инициализации объектов теперь требуется передать параметры:
car_0 = Car('green', 10)
print(car_0.gas_tank)
print(car_0.color)

car_1 = Car('black', 10)
car_2 = Car('yellow', 10)

print('car_0', car_0.position)
print('car_1', car_1.position)
print('car_2', car_2.position)

car_0.position[1] = 2 # ссылка на один и тот же список

print('car_0', car_0.position)
print('car_1', car_1.position)
print('car_2', car_2.position)
# изменился атрибут класса, а не объекта:
print(Car.__dict__)
print(car_0.__dict__)
print(car_1.__dict__)
print(car_2.__dict__)
# чтобы такого не происходило, нужно все атрибуты поместить в инициализатор
