class Zad4:
    firstArray = []
    secondArray = []

    def __init__(self, firstArray, secondArray):
        self.firstArray = firstArray
        self.secondArray = secondArray

    def search_array(self, targetNumber):
        for i in self.firstArray:
            for j in self.secondArray:
                if i + j == targetNumber:
                    return [i, j]
