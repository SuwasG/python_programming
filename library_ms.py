class Book:
    def __init__(self, title, author, isbn):
        self.title=title 
        self.author=author
        self.isbn=isbn
        self.available=True

class Library:
    def __init__(self):
        self.books=[]
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    
    def show_books(self):
        available_books=[]
        for book in self.books:
            if book.available:
                available_books.append(book) 
        return available_books
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book 
        return None 
    
    def book_details(self, title):
        book=self.find_book(title)
        if book:
            print("Book Details:")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"ISBN: {book.isbn}")
            print(f"Availability: {'Available' if book.available else 'Borrowed'}")
        else:
            print("Book not found.")
        
    def borrow_book(self, title):
        book = self.find_book(title)
        if book and book.available:
            book.available=False 
            return book 
        return None
    
    def return_book(self, title):
        book = self.find_book(title)
        if book and not book.available:
            book.available = True
            return book
        return None


# Example usage:
library = Library()

book1 = Book("Python Programming", "Suwas Ghale", "123456789")
book2 = Book("Machine Learning", "Suwas Lama", "987654321")
book3 = Book("Cyber Security", "Suwas Don", "987654321")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

available_books = library.show_books()
print("Available Books:")
for book in available_books:
    print(book.title)

library.book_details("Python Programming")

borrowed_book=library.borrow_book("Python Programming")
if borrowed_book:
        print(f"{borrowed_book.title} is borrowed.")
else:
    print(f"{borrowed_book.title} is not available.")

library.book_details("Python Programming")
library.book_details("Machine Learning")


available_books2 = library.show_books()
print("Available Books2:")
for book in available_books2:
    print(book.title)

returned_book = library.return_book("Machine Learning")
if returned_book:
    print(f"{returned_book.title} is returned.")
else:
    print("Book not found.")

returned_book2 = library.return_book("Python Programming")
if returned_book2:
    print(f"{returned_book2.title} is returned.")
else:
    print("Book not found.")


