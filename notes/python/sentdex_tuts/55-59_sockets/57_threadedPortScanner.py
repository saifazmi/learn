# A threaded port scanner

import socket
import threading
from queue import Queue

print_lock = threading.Lock()

target = "pythonprogramming.net"

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print("Port", port, "is OPEN!")
        con.close()
    except:
        pass # lets not waste print statements with print_lock

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


q = Queue()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,501): # since port zero is an invalid port
    q.put(worker)

q.join()
