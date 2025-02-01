class Employee:
    def __init__(self,name=None,id=None,department=None):
        self.name=name
        self.id=id
        self.department=department
e=Employee()
e.name="Ram"
e.id=123
e.department="Analyst"
print("Name: ",e.name)
print("id: ",e.id)
print("department: ",e.department)