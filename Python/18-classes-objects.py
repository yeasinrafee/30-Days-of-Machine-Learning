class MyClass:
    x = 5 
p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p2 = Person("Rafee", 24)
print(p2.name)
print(p2.age)

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old!") 
    def __str__(self):
        return f"{self.name} {self.age}"
p3 = Person2("Yeasin", 22)
print(p3)
p3.myfunc()