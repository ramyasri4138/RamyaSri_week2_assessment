class Animal:
    def speak(self):
        print("Animals sound")
class Dog(Animal):
    def speak(self):
        return "Bow Bow"
class Cat(Animal):
    def speak(self):
        return "Meow Meow"
d=Dog()
c=Cat()
a=Animal()
print(d.speak())
print(c.speak())