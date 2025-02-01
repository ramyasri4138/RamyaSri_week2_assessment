class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print("The Book Details are: ")
        print("The tile of book: ",self.title)
        print("The author of book: ",self.author)
        print("The isbn of book: ",self.isbn)
b=Book("Ramayanam","Valmiki",1234)
b.display()