from book import Book
from review import Review


class User:
    def __init__(self, user_name, password):
        if isinstance(user_name, str) and len(user_name.strip()) != 0:
            self._user_name = (user_name.strip()).lower()
        else:
            self._user_name = None
        if isinstance(password, str) and len(user_name.strip()) >= 7:
            self._password = password
        else:
            self._password = None
        self._read_books = []
        self._reviews = []
        self._pages_read = 0

    @property
    def user_name(self):
        return ((self._user_name).lower()).strip()

    @property
    def password(self):
        return self._password

    @property
    def read_books(self):
        return self._read_books

    @property
    def reviews(self):
        return self._reviews

    @property
    def pages_read(self):
        return self._pages_read

    def __repr__(self):
        return f'<User {self._user_name}>'

    def __eq__(self, other):
        if isinstance(other, User):
            if self._user_name == other._user_name:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, User):
            return self._user_name < other._user_name
        else:
            return False

    def __hash__(self):
        return hash(self._password)

    def read_a_book(self, book):
        if isinstance(book, Book):
            self._read_books.append(book)
            self._pages_read += book.num_pages

    def add_review(self, review):
        if isinstance(review, Review):
            self._reviews.append(review)

#   @user_name.setter
#    def user_name(self, user):
#        if isinstance(user, str):
#            self._user_name = (user.strip()).lower()
#        else:
#            self._user_name = None

#    @password.setter
#    def password(self, p):
#        if len(p) > 7 and isinstance(p, str):
#            self._password = p
#        else:
#            self._password = None
