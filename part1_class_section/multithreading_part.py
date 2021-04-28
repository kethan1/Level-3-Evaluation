"""
Multithreading
1.	Give an example of the following for threads.
a.	Creating
b.	Starting

2.	Explain the concept of multithreading and the objective of using it.
Multithreading can be to have two pieces of code run concurrently. For example when implementing
full duplex communication, the sending and recieving has to be run concurrently. 
"""

import threading
import time

def print_stuff():
    time.sleep(int(input("enter time: ")))

def print_stuff2():
    time.sleep(int(input("enter time: ")))

t = threading.Thread(target=print_stuff, daemon=True)
t.start()

t2 = threading.Thread(target=print_stuff2, daemon=True)
t2.start()

while True:
    if not t.is_alive():
        print("Thread 1 finished first")
        t2.join()
        break
    elif not t2.is_alive():
        print("Thread 2 finished first")
        t.join()
        break
