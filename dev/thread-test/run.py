import time
from threading import Thread
from threading import Lock

class var_obj:
    def __init__(self):
        self.value = 1

def a(obj):
    for i in range(10000000):
        obj.value = obj.value + 1

def b():
    o = var_obj()
    print("1:{}".format(o.value))
    a(o)
    print("2:{}".format(o.value))
    Thread(target=a, args=(o,)).start()
    Thread(target=a, args=(o,)).start()
    time.sleep(0.1)
    print("3:{}".format(o.value))
    time.sleep(0.1)
    print("4:{}".format(o.value))
    time.sleep(0.1)
    print("5:{}".format(o.value))

b()

