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