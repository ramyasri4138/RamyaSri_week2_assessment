class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,quantity):
        if quantity<=self.stock:
            return "available"
        else:
            return "Not available"
p=Product("BHAGAVATH BOOK","200",100)
print(p.check_availability(90))
print(p.check_availability(101))