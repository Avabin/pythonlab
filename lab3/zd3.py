import time
import threading

lockedWC = False


class WCLocker:
    locked = False

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def is_locked(self):
        return self.locked

wc = WCLocker()


class Customer(threading.Thread):
    def __init__(self, wc):
        super().__init__()
        self.wc = wc

    def run(self):
        while 1:
            if not self.wc.is_locked():
                self.wc.lock()
                print("wątek ", threading.current_thread().name, "wchodzi do toalety i robi co musi")
                time.sleep(5)
                print("wątek ", threading.current_thread().name, "opuszcza toaletę")
                self.wc.unlock()
                time.sleep(1)

for x in range(4):
    t = Customer(wc)
    t.start()