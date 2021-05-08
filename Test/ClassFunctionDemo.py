class MyClass():
    name = "swathi"
    def sum(self, a, b):
        print(a+b)
    def __init__(self, name, age):
        self.name= name
        self.age=age


x= MyClass("john", 30)
print(x.name)
x.sum(4,5)
print(x.age)