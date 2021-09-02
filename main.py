from author import Author
from book import Book
from booksJSONreader import BooksJSONReader
from booksinventory import BooksInventory
from publisher import Publisher
from review import Review
from user import User


def main():
    authors_filename = 'book_authors_excerpt.json'
    books_filename = 'comic_books_excerpt.json'
    reader = BooksJSONReader(books_filename, authors_filename)
    reader.read_json_files()

    print(reader.dataset_of_books[4].title)
    print(reader.dataset_of_books[4].release_year)
    print(reader.dataset_of_books[4].description)

main()