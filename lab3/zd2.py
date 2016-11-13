from threading import *
from time import *


class Barman(Thread):
    def __init__(self, glass):
        super().__init__()
        self.setName("Barman")
        self.glass = glass

    def run(self):
        while 1:
            sleep(1.321)
            self.fill_glass()

    def fill_glass(self):
        if not self.glass.locked:
            if not self.glass.filled:
                self.glass.lock()
                print(self.getName(), "\t:\t Here comes your drink, sir.")
                self.glass.fill()
                self.glass.unlock()


class Client(Thread):
    def __init__(self, glass):
        super().__init__()
        self.setName("Client")
        self.glass = glass

    def run(self):
        print(self.getName(), "\t:\t Barman! Get me drink!")
        while 1:
            sleep(1)
            self.drink()

    def drink(self):
        if not self.glass.locked:
            if self.glass.filled:
                self.glass.lock()
                print(self.getName(), "\t:\t Thank you. Cheers!")
                self.glass.empty()
                print(self.getName(), "\t:\t Get me next drink.")
                self.glass.unlock()
            else:
                print(self.getName(), "\t: \t Hey, barman! My glass is empty!")


class Glass():

    locked = False
    filled = False

    def fill(self):
        self.filled = True

    def empty(self):
        self.filled = False

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

glass = Glass()
barman = Barman(glass)
client = Client(glass)

barman.start()
client.start()