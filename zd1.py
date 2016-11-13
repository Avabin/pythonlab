class Triangle:
    number_of_sides = 3

    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def check_angles(self):
        return self.a1 + self.a2 + self.a3 == 180

    def __eq__(self, other):
        if self.a1 == other.a1 and \
                        self.a2 == other.a2 and \
                        self.a3 == other.a3:
            return True
        else:
            return False
