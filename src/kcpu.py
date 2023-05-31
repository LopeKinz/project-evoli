import time

def kill_cpu1():
    while True:
        time.sleep(0.001)  # Give other programs a false sense of hope

import multiprocessing

def kill_cpu2():
    while True:
        multiprocessing.Pool().map(lambda x: x**x, range(999999))

# Please note that running this function can cause your computer to freeze or crash. Use it responsibly and at your own risk.
