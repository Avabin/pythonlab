import _thread
import threading
import time


def do(threadName, sleeptime):
    while 1:
        print(threadName)
        time.sleep(sleeptime)


class Test(threading.Thread):
    def __init__(self, name, sltime):
        super(Test, self).__init__()
        self.threadName = name
        self.sleeptime = sltime

    def run(self):
        do(self.threadName, self.sleeptime);

x = list()
for i in (1, 2):
    x.append(Test("THREAD-" + str(i), 2))
    x[i - 1].start()
