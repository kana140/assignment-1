import json

from author import Author
from book import Book
from publisher import Publisher


class BooksJSONReader:
    def __init__(self, books_file_name, authors_file_name):
        if isinstance(books_file_name, str) and len(books_file_name.strip()) != 0:
            self._books_file_name = books_file_name
        else:
            raise ValueError("ValueError was raised!")
        if isinstance(authors_file_name, str) and len(authors_file_name.strip()) != 0:
            self._authors_file_name = authors_file_name
        else:
            raise ValueError("ValueError was raised!")
        self._dataset_of_books = []

    @property
    def dataset_of_books(self):
        return self._dataset_of_books

    def read_json_files(self):
        try:
            f1 = open(self._books_file_name)
            f2 = open(self._authors_file_name)
            books = f1.readlines()
            authors = f2.readlines()
            #for line in authors:
            #    authors_dict = json.loads(line) #loads a dictionary
            for b in books:
                books_dict = json.loads(b)
                book_object = Book(int(books_dict.get("book_id")), books_dict.get("title"))
                book_object.publisher = Publisher(books_dict.get("publisher"))
                if len(books_dict.get("publication_year")) != 0:
                    book_object.release_year = int(books_dict.get("publication_year"))
                book_object.description = books_dict.get("description")
                author_list = books_dict.get("authors")
                for item in author_list: #item is a dictionary item
                    author_id = item.get("author_id")
                    for a in authors:
                        authors_dict = json.loads(a)
                        if author_id == authors_dict.get("author_id"):
                            book_object.add_author(Author(int(authors_dict.get("author_id")), authors_dict.get("name")))
                self.dataset_of_books.append(book_object)
        except FileNotFoundError:
            raise ValueError("ValueError was raised!")
