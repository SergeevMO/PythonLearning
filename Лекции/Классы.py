class Car:
    color = 'black'
    body = 'regular'
    gas_tank = 0 # l
    max_speed = 200 # km/h
    position = 0
    state = 'stopped'
    speed = 0 # km/h

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



car_0 = Car()
car_1 = Car()

print(car_0)
print(car_1)
print(car_0 is car_1)
print('outside class: ', car_0)
car_0.start()
print(car_1.color)
car_1.color = 'green'
print(car_1.color)

print(car_0.gas_tank)
print(car_1.gas_tank)
car_0.fill_gas_tank(10)
car_1.fill_gas_tank(40)
print(car_0.gas_tank)
print(car_1.gas_tank)

print(car_0.speed)
car_0.accelerate(100)
print(car_0.speed)
car_0.accelerate(50)
print(car_0.speed)
car_0.accelerate(70)
print(car_0.speed)


# данные для каждого объекта хранятся в __dict__, представляющего собой словарь
print(car_0.__dict__)
print(car_1.__dict__)
# если при обращении к объекту запрашиваемого аттрибута нет,
# то за его значением обращаются к словарю класса Сar.__dict__
print(Car.__dict__)
# все классы наследуются от базового класса type
# все сущности являются объектами
print(type(Car))
print(type(car_0))
print(type(car_1))
# тип класса - type
# тип объекта класса - __main__.Car
# в type содержатся все методы, которые определяют дочерние объекты
