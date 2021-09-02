from book import Book

class BooksInventory:
    def __init__(self):
        self._book_dictionary = {}

    def add_book(self, book, price, nr_books_in_stock):
        if isinstance(book, Book) and (isinstance(price, int) or isinstance(price, float)) and isinstance(nr_books_in_stock, int) and price >= 0 and nr_books_in_stock >= 0:
            self._book_dictionary[book.book_id, book.title] = [book, price, nr_books_in_stock]
        else:
            raise ValueError("ValueError was raised!")

    def remove_book(self, book_id):
        for key in self._book_dictionary.keys():
            if book_id in key:
                self._book_dictionary.pop(key)
                return
        return None


    def find_book(self, book_id):
        for key in self._book_dictionary.keys():
            if isinstance(book_id, int) and book_id in key:
                return self._book_dictionary[key][0]
        return None

    def find_price(self, book_id):
        for key in self._book_dictionary.keys():
            if isinstance(book_id, int) and book_id in key:
                return self._book_dictionary[key][1]
        return None

    def find_stock_count(self, book_id):
        for key in self._book_dictionary.keys():
            if isinstance(book_id, int) and book_id in key:
                return self._book_dictionary[key][2]
        return None

    def search_book_by_title(self, title):
        for key in self._book_dictionary.keys():
            if isinstance(title, str) and title in key:
                return self._book_dictionary[key][0]
        return None