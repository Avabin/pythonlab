from threading import *
from time import sleep


class CalcT1(Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        sleep(1)
        self.num = pow(self.num, self.num)
        print(self.getName(), "\t:\t", self.num)


class CalcT2(Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        self.num //= self.num - 1
        print(self.getName(), "\t:\t", self.num)


class CalcT3(Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        sleep(2)
        self.num = hex(int (self.num / 1725))
        print(self.getName(), "\t:\t", self.num)

x, y, z = CalcT1(12), CalcT2(12387), CalcT3(9127)

x.start()
y.start()
while 1:
    if not (x.is_alive() or y.is_alive()):
        z.start()
        break
