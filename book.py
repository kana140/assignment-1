from author import Author
from publisher import Publisher


class Book:
    def __init__(self, book_id, title):
        if isinstance(title, str) and len(title.strip()) != 0:
            self._title = title.strip()
        else:
            raise ValueError("ValueError was raised!")
        if isinstance(book_id, int) and book_id >= 0:
            self._book_id = book_id
        else:
            raise ValueError("ValueError was raised!")
        self._description = ""
        self._publisher = None
        self._release_year = 0
        self._authors = []
        self._ebook = None

    @property
    def book_id(self):
        return self._book_id

    @property
    def title(self):
        return (self._title).strip()

    @title.setter
    def title(self, t):
        if isinstance(t, str) and len(t.strip()) != 0:
            self._title = t.strip()
        else:
            raise ValueError("ValueError was raised!")

    @property
    def description(self):
        return (self._description).strip()

    @description.setter
    def description(self, d):
        if isinstance(d, str) and len(d.strip()) != 0:
            self._description = d.strip()
        else:
            pass

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, p):
        if isinstance(p, Publisher):
            self._publisher = p
        else:
            pass

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, a):
        if isinstance(a, list):
            for e in a:
                if not(isinstance(e, Author)):
                    return
            self.authors = a
        else:
            pass

    @property
    def release_year(self):
        return self._release_year

    @release_year.setter
    def release_year(self, ry):
        if isinstance(ry, int) and ry >= 0:
            self._release_year = ry
        else:
            raise ValueError("ValueError was raised!")

    @property
    def ebook(self):
        return self._ebook

    @ebook.setter
    def ebook(self, e):
        if isinstance(e, bool):
            self._ebook = e
        else:
            pass

    def __repr__(self):
        return f'<Book {self.title}, book id = {self.book_id}>'

    def __eq__(self, other):
        if isinstance(other, Book):
            if self.book_id == other.book_id:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.book_id < other.book_id
        else:
            return False

    def __hash__(self):
        return hash(self.book_id)

    def add_author(self, author):
        if isinstance(author, Author):
            if author not in self.authors:
                self.authors.append(author)
            else:
                return
        else:
            return

    def remove_author(self, author):
        if isinstance(author, Author):
            if author in self.authors:
                self.authors.remove(author)
            else:
                return
        else:
            return



