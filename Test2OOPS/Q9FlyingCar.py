class Car:
    def __init__(self):
        pass
    def move(self):
        print("It moves on road")
class Airplane:
    def __init__(self):
        pass
    def move(self):
        print("It Flies")
class FlyingCar(Car,Airplane):
    def __init__(self):
        super().__init__()
    def move(self):
        print("Flying Car can fly in sky and move on road")
        movement=input("Enter either fly Or drive: ")
        if movement=="fly":
            Airplane.move(self)
        elif movement=="drive":
            Car.move(self)
f=FlyingCar()
f.move()           
        
        
