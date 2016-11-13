class Person:
    name = ""
    age = -1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        assert isinstance(other, Person)
        if (self.name == other.name) and (self.age == other.age):
            return True
        else:
            return False

    def __ne__(self, other):
        if (self.name != other.name) or (self.age != other.age):
            return True
        else:
            return False

    def __lt__(self, other):
        assert isinstance(other, Person)
        if self.name == other.name:
            return self.age < other.age
        else:
            return self.name < other.name
