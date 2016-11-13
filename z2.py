class Zad2:
    number = -1
    MAX = 3999
    MIN = 1
    rome_array = []

    def __init__(self, number):
        if number < self.MIN or number > self.MAX:
            raise ArithmeticError
        else:
            self.number = number
        self.rome_array = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'LC', 'C', 'CD', 'D', 'DM', 'M']
        self.arab_array = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    def add_num(self, roman_number, arab_number):
        toreturn = ''
        while 1:
            if self.number >= arab_number:
                self.number -= arab_number
                toreturn += roman_number
            else:
                return toreturn

    def get_converted_number(self):
        converted = ''
        for arab, roman in reversed(list(zip(self.arab_array, self.rome_array))):
            converted += self.add_num(roman, arab)
        return converted
