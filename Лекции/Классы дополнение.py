class Foo:
    def pr():
        return 100

    def fy(self):
        return self

    def uk(self):
        temp = pr() # нельзя обратиться к функции без self
        return temp

foo_1 = Foo()

print(Foo())
print(foo_1)
print(foo_1.fy())
# print(foo_1.pr()) # нельзя вызвать функцию без self
# print(foo_1.uk()) # нельзя вызвать функцию, ссылающуюся на функцию без self
print(Foo.__dict__)
print(foo_1.__dict__)

# покак никаких атрибутов у класса и его объекта нет
# но объекту можно добавить атрибут путём указания имени и значения:
foo_1.taram = 147
print(Foo.__dict__)
print(foo_1.__dict__)
print(foo_1.taram)