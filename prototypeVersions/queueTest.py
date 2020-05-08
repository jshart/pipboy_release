import queue
import random
import threading
import time
import sys
q = queue.Queue()

def generator():
    global q
    global alive
    i=0
    while alive==True:
        time.sleep(0.1)
        q.put(i)
        i=i+1
        
        
def consumer():
    global q
    global alive
    while alive==True:
        time.sleep(0.2)
        print("L:{:d}V:{:d}".format(q.qsize(),q.get()))
        
alive=True
generatorThread = threading.Thread(target=generator)
generatorThread.daemon=True
consumerThread = threading.Thread(target=consumer)
consumerThread.daemon=True

generatorThread.start()
consumerThread.start()

a = input("press return to quit")
alive=False
#exit(0)
