class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move...!!")
        
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail...!!")
        
class Plane(Vehicle):
    def move(self):
        print("Fly...!!")
        
car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

for x in (car, boat, plane):
    print(x.brand)
    print(x.model)
    x.move()