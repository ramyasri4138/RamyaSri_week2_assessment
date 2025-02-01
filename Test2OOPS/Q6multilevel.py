class Vehicle():
    def sound(self):
        pass
class Bike(Vehicle):
    def wheels(self):
        print("Bike has Two wheels")
class Car(Vehicle):
    def wheels(self):
        print("Car has Four wheels")
class ElectricCar(Car):
    def sound(self):
        print("No sound")
    def wheels(self):
        super().wheels()
        print("Electric car has four wheels")
        
b=Bike()
e=ElectricCar()
e.sound()
e.wheels()