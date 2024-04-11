class Book:
    def __init__(self, book_name, author):
        self.__book_name = book_name
        self.__author = author

    def print_book(self):
        print(f"Name : {self.__book_name}, Author : {self.__author}")


class Library:
    def __init__(self, books: list[Book], no_of_books: int):
        self.__books = books
        self.__no_of_books = no_of_books

    def show_all_books(self):
        if self.check_no_of_books():
            print(f"Registered No of Books : {self.__no_of_books}")
            for book in self.__books:
                book.print_book()

    def add_book(self, book: Book):
        self.__books.append(book)
        # self.__no_of_books += 1

    def check_no_of_books(self) -> bool:
        """checks if the no of books in library and registered no of books are same"""
        if len(self.__books) < self.__no_of_books:
            print(
                f"No of books {len(self.__books)} is less than the registered No of book {self.__no_of_books}")
            return False
        else:
            return True


bookList: list[Book] = [Book("Java", "Java Author"), Book("Python", "PythonAuthor"),
                        Book("C++", "C++ Author")]

library = Library(bookList, 4)
library.show_all_books()
library.add_book(Book("C", "C Author"))
print("------")
library.show_all_books()
