class Person():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        
class Employee(Person):
    def __init__(self, name, gender,e_id):
        super().__init__(name, gender)
        self.e_id=e_id
    
class Manager(Employee):
    def __init__(self,name,gender,e_id,dept):
        super().__init__(name,gender,e_id)
        self.dept=dept
    def approve_leave(self,no_of_days):
        if no_of_days>3:
            print(f"name:{self.name} and gender:{self.gender} with emp_id:{self.e_id} has no leaves")
        else:
            print(f"name:{self.name} and gender:{self.gender} with emp_id:{self.e_id} can Take Leave")

m=Manager("Shiva","Male",12222232,"Information Technology")
p=Person("Ram","Male")
print(m.approve_leave(3))

        