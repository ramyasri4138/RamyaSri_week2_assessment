from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Data inserted in SQl Databsase")
    def update(self):
        print("Data updated in SQL ")
    def delete(self):
        print("data deleted in Sql")
        
class NOSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("data inserted in nosql")
    def update(self):
        print("Data updated in noSQL ")
    def delete(self):
        print("data deleted in noSql")
        
s=SQLDatabase()
n=NOSQLDatabase()
s.insert()
s.update()
s.delete()
n.insert()
n.update()
n.delete()