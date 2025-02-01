from abc import ABC,abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(IShape):
    def calculate_area(self,side):
        print(f"Area of Rectangle is {side*side}")
class Circle(IShape):
    def calculate_area(self,radius):
        print(f"The area of circle is {3.14*radius*radius}")

r=Rectangle()
c=Circle()  
r.calculate_area(3)
c.calculate_area(3)  