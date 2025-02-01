class Electronics:
    def __init__(self,company):
        self.company=company
    def work(self):
        print("ViJAY Electronics")
class MobileDevice(Electronics):
    def __init__(self,company,brand):
        super().__init__(company)
        self.brand=brand
    
class SmartPhone(MobileDevice):
    def __init__(self,company,brand,version):
        super().__init__(company,brand)
        self.version=version
    def work(self):
        print(f"company:{self.company}, brand, {self.brand}, version:{self.version}")
        
s=SmartPhone("Samsung","Galaxy","g16")
s.work()