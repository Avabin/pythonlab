class Zad1:
    str = ""

    def __init__(self):
        self.str = "hello.py"

    def get_result(self):
        self.str = self.str.partition('.')
        return self.str[1] + self.str[2] + ' ' + self.str[0]
