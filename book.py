class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    
    def describe(self):
        print(f"Title: {self.title}, Author: {self.author}, Year Published: {self.year_published}")

# Creating three book objects
book1 = Book("To Kill a Mockingbird", "jhon lester", 1960)
book2 = Book("1984", "mcgregor", 1949)
book3 = Book("The Great Gatsby", "bongbong marcos", 1925)

# Displaying book details
book1.describe()
book2.describe()
book3.describe()