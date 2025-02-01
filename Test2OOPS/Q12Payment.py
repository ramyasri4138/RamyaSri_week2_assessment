class Payment:
    def __init__(self,amount):
        self.amount=amount
    def process_payment():
        pass
class CreditCardPayment(Payment):
    def process_payment(self):
        print(f"{self.amount} paid by creditCard")
class PayPalPayment(Payment):
    def process_payment(self):
        print(f"{self.amount} paid by PayPalPayment")
class  BitcoinPayment(Payment):
    def process_payment(self):
        print(f"{self.amount} paid by the Bitcoin Payment")
        
c=CreditCardPayment(100)
p=PayPalPayment(200)
b=BitcoinPayment(200)
c.process_payment()
p.process_payment()
b.process_payment()