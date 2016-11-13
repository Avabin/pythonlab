import threading
import time


class CalculateThread(threading.Thread):
    def __init__(self, num):
        super(CalculateThread, self).__init__()
        self.num = num

    def run(self):
        while 1:
            self.num += 3
            print(threading.get_ident(), "\t:\t", self.getName(), "\t:\t", self.num)
            if not self.num % 2:
                time.sleep(2)


x = [CalculateThread(19), CalculateThread(109)]

for thread in x:
    thread.start()
