import datetime

class Book:
    def __init__(self, name, ISBN, Author):
        self.name = name
        self.ISBN = ISBN
        self.Author = Author

    def print_book_details(self):
        print(self.name, self.ISBN, self.Author)


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {} #Dictionary
        self.issued_books = {}

    def print_all_books(self):
        print(f"==========={self.name} has following books===========")
        for book, copies in self.books.items():
            print(f"{book.name} {book.ISBN} {book.Author} {copies} copies ")
        print(f"=================================================================")
        return self.books


class Student:
    def __init__(self, name, year,books):
        self.name = name
        self.year = year
        self.books = {}

    def print_all_my_books(self):
        for b in self.books.keys():
            print(self.name," has ",b.name, "ISBN:", b.ISBN,"Author:", b.Author,"Issue date:",self.books[b], end=" ")
        print("\n")


class Librarian:

    def __init__(self, name, library):
        self.name = name
        self.library = library

    def add_book(self, book, copies):
        if book in self.library.books.keys():
            return "Book record already exists"
        self.library.books[book] = copies
        return "Book record added"

    def remove_book(self, book):
        if book in self.library.books.keys():
            del self.library.books[book]
            return "Book record removed"
        return "Book record unavailable"

    def issue_book(self, book, student, date):
        for bk in self.library.books.keys():
            if bk.name == book.name:
                self.library.books[book] -= 1
                student.books[book]=date
                return student
        else:
            return "Book unavailable"


    def check_late_returns(self, student):
        for book in student.books.keys():
            if (datetime.date.today() - student.books[book]).days >5:
                print(f"Book {book.name} is due for return")


if __name__ == '__main__':
    St_Xaviers_Library = Library("St_Xaviers Library")
    print(St_Xaviers_Library.print_all_books())

    Miss_Briganza = Librarian("Miss_Briganza", St_Xaviers_Library)

    rahul = Student("Rahul", 3, [])
    anjali = Student("anjali", 1, [])
    tina = Student("tina", 1, [])

    book1 = Book("Romeo and Juliet", "T6JSS", "Shakespeare")
    book2 = Book("Harry Potter", "SAW77", "J. K. Rowling")
    book3 = Book("Quantitative Aptitude", "GAM875", "R. S. Aggarwal")
    book4 = Book("Concepts of Physics", "LSG3723", "H. C. Verma")

    result = Miss_Briganza.add_book(book1, 10)
    rahul = Miss_Briganza.issue_book(book1, rahul, datetime.date(2020,7,1))
    rahul.print_all_my_books()
    Miss_Briganza.library.print_all_books()

    Miss_Briganza.check_late_returns(rahul)