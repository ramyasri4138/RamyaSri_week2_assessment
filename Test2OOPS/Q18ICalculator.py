from abc import ABC,abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    @abstractmethod
    def subtract(self,a,b):
        pass
    @abstractmethod
    def multiply(self,a,b):
        pass
    @abstractmethod
    def divide(self,a,b):
        pass
class BasicCalculator(ICalculator):
    def add(self,a,b):
        print(a+b)
    def subtract(self, a, b):
        print(a-b)
    def multiply(self, a, b):
        print(a*b)
    def divide(self,a,b):
        print(a/b)
b=BasicCalculator()
b.add(8,2)
b.subtract(8,2)
b.multiply(8,2)
b.divide(8,2)