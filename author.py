class Author:
    def __init__(self, author_id, author_full_name):
        if isinstance(author_id, int) and author_id >= 0:
            self._unique_id = author_id
        else:
            raise ValueError("ValueError was raised!")
        if isinstance(author_full_name, str) and len(author_full_name.strip()) != 0:
            self.full_name = author_full_name
        else:
            raise ValueError("ValueError was raised!")
        self._author_list = [self._unique_id]

    @property
    def full_name(self):
        return (self._full_name).strip()

    @full_name.setter
    def full_name(self, fn):
        if isinstance(fn, str):
            if len(fn.strip()) != 0:
                self._full_name = fn.strip()
            else:
                raise ValueError("ValueError was raised!")
        else:
            raise ValueError("ValueError was raised")

    @property
    def unique_id(self):
        return self._unique_id

    def __repr__(self):
        return f'<Author {self.full_name}, author id = {self.unique_id}>'

    def __eq__(self, other):
        if isinstance(other, Author):
            if self.unique_id == other.unique_id:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Author):
            return self.unique_id < other.unique_id
        else:
            return False

    def __hash__(self):
        return hash(self.unique_id)

    def add_coauthor(self, coauthor):
        if isinstance(coauthor, Author):
            self._author_list.append(coauthor.unique_id)
            coauthor._author_list.append(self.unique_id)

    def check_if_this_author_coauthored_with(self, author):
        if isinstance(author, Author):
            for element in self._author_list:
                if author.unique_id == element:
                    return True
            return False
        else:
            return False

