import unittest
from LibraryManagementMain import Book, Student, Librarian, Library


class TestCases(unittest.TestCase):

    St_Xaviers_Library = Library("St_Xaviers Library")
    Miss_Briganza = Librarian("Miss_Briganza", St_Xaviers_Library)

    rahul = Student("Rahul", 3, [])
    anjali = Student("anjali", 1, [])
    tina = Student("tina", 1, [])

    book1 = Book("Romeo and Juliet", "T6JSS", "Shakespeare")
    book2 = Book("Harry Potter", "SAW77", "J. K. Rowling")
    book3 = Book("Quantitative Aptitude", "GAM875", "R. S. Aggarwal")
    book4 = Book("Concepts of Physics", "LSG3723", "H. C. Verma")

    def test_librarian_add_book(self):
        self.assertEqual("Book record added", self.Miss_Briganza.add_book(self.book1, 10))
        self.assertEqual("Book record added", self.Miss_Briganza.add_book(self.book2, 10))
        self.assertEqual("Book record added", self.Miss_Briganza.add_book(self.book3, 10))
        self.assertEqual("Book record added", self.Miss_Briganza.add_book(self.book4, 10))
        # self.assertEqual("Book record added", self.Miss_Briganza.add_book(self.book1, 10))
        self.assertEqual("Book record already exists", self.Miss_Briganza.add_book(self.book1, 10))

    def test_librarian_remove_book(self):
        self.assertEqual("Book record removed", self.Miss_Briganza.remove_book(self.book1))
        # self.assertEqual("Book record removed", self.Miss_Briganza.remove_book(self.book1))
        self.assertEqual("Book record unavailable", self.Miss_Briganza.remove_book(self.book1))

    def test_print_all_books(self):
        self.assertEqual(3, len(self.St_Xaviers_Library.print_all_books()))

if __name__ == '__main__':
    unittest.main()
