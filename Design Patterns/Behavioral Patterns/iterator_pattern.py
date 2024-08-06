from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> object:
        pass

class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

class Book:
    def __init__(self, title: str) -> None:
        self._title = title

    def get_title(self) -> str:
        return self._title

class BookCollection(Aggregate):
    def __init__(self) -> None:
        self._books = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def create_iterator(self) -> Iterator:
        return BookIterator(self._books)

class BookIterator(Iterator):
    def __init__(self, books: list) -> None:
        self._books = books
        self._position = 0

    def has_next(self) -> bool:
        return self._position < len(self._books)

    def next(self) -> Book:
        book = self._books[self._position]
        self._position += 1
        return book


if __name__ == "__main__":
    book1 = Book("Design Patterns: Elements of Reusable Object-Oriented Software")
    book2 = Book("Clean Code: A Handbook of Agile Software Craftsmanship")
    book3 = Book("Refactoring: Improving the Design of Existing Code")

    book_collection = BookCollection()
    book_collection.add_book(book1)
    book_collection.add_book(book2)
    book_collection.add_book(book3)

    iterator = book_collection.create_iterator()

    while iterator.has_next():
        book = iterator.next()
        print(book.get_title())
