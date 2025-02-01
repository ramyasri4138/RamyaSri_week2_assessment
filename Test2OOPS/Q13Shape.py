class Shape:
    def area(self):
        pass
class Square(Shape):
    def area(self,side):
        print(f"Area is: {side*side}")
class Traingle(Shape):
    def area(self,b,h):
        print(f"Area is: {(b*h)/2}")
s=Square()
t=Traingle()
sh=Shape()
s.area(2)
t.area(3,4)