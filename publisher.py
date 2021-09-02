class Publisher:
    def __init__(self, name):
        if isinstance(name, str) and len(name.strip()) != 0:
            self.name = name
        else:
            self.name = "N/A"

    @property
    def name(self):
        string = self._name
        return string.strip()

    @name.setter
    def name(self, value):
        if (type(value) != str) or len(value.strip()) == 0:
            self._name = "N/A"
        else:
            self._name = value.strip()

    def __repr__(self):
        return f'<Publisher {self.name}>'

    def __eq__(self, other):
        if isinstance(other, Publisher):
            if self.name == other.name:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Publisher):
            return self.name < other.name
        else:
            return False

    def __hash__(self):
        return hash(self.name)

