class Zad3:
    numberList = list()
    numarray = []

    def __init__(self, numarray):
        self.numarray = numarray

    def recursive_lists(self):
        if len(self.numarray) != 0:
            self.numberList.append(self.numarray)
            self.numarray = self.numarray[:-1]
            self.recursive_lists()

    def do(self):
        self.recursive_lists()
        return self.numberList
