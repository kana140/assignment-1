import datetime
from book import Book


class Review:
    def __init__(self, book, review_text, rating):
        if isinstance(book, Book):
            self._book = book
        else:
            self._book = None
        if isinstance(review_text, str) and len(review_text.strip()) != 0:
            self._review_text = review_text.strip()
        else:
            self._review_text = "N/A"
        if isinstance(rating, int) and (rating >= 1 and rating <= 5):
            self._rating = rating
        else:
            raise ValueError("ValueError was raised!")
        self._timestamp = datetime.datetime.now()

    @property
    def book(self):
        return self._book

    @property
    def review_text(self):
        return (self._review_text).strip()

    @property
    def rating(self):
        return self._rating

    @property
    def timestamp(self):
        return self._timestamp

    def __repr__(self):
        return f'<Book {self.book.title}, rating = {self.rating}, timestamp = {self.timestamp}>'

    def __eq__(self, other):
        if isinstance(other, Review):
            if self.book != other.book:
                return False
            if self.review_text != other.review_text:
                return False
            if self.rating != other.rating:
                return False
            if self.timestamp != other.timestamp:
                return False
            return True
        else:
            return False