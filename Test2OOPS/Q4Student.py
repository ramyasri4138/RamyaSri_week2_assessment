class Student:
    def __init__(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum
    def display_details(self):
        return f"Name: {self.name} and Roll number: {self.rollnum}"
s=Student("Shiva",1234)
print(s.display_details())