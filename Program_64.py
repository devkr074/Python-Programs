# Polymorphism in Python

print(f"\nFunction Polymorphism\n")
x="Hello World!"
print(len(x))
myTuple=("Apple","Banana","Cherry")
print(len(myTuple))
myDict={
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}
print(len(myDict))
print(f"\nClass Polymorphism\n")
class Car:
    def __init__(self,brand,model):
       self.brand=brand
       self.model=model
    def move(self):
       print("Drive!")
class Boat:
    def __init__(self,brand,model):
       self.brand=brand
       self.model=model
    def move(self):
       print("Sail!")
class Plane:
    def __init__(self,brand,model):
       self.brand=brand
       self.model=model
    def move(self):
       print("Fly!")
car1=Car("Ford","Mustang")
boat1=Boat("Ibiza","Touring 20")
plane1=Plane("Boeing","747")
for x in (car1,boat1,plane1):
   x.move()
print(f"\nInheritance Class Polymorphism\n")
class Vehicle:
    def __init__(self,brand,model):
       self.brand=brand
       self.model=model
    def move(self):
       print("Move!")
class Car(Vehicle):
   pass
class Boat(Vehicle):
    def move(self):
       print("Sail!")
class Plane(Vehicle):
    def move(self):
       print("Fly!")
car1=Car("Ford","Mustang")
boat1=Boat("Ibiza","Touring 20")
plane1=Plane("Boeing","747")
for x in (car1,boat1,plane1):
   print(x.brand)
   print(x.model)
   x.move()