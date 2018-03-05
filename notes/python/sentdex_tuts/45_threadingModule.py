# Threading module

'''
' One of the largest drawback of Python is that it is single-threaded.
' So for a large computational task one can notice that Python is taking
' a large amount of time, even though the processor is sitting at 5% usasge
'
' There are a few solutions for this problem, like threading, multiprocessing
' and GPU programming. All of these are possible with Python. Here we will look
' at threading.
'
' The idea behind threading is that you can perform multiple tasks
' simultaneously. One thing that can cause trouble very quickly with threading
' is shared variables between tasks, and they are trying to update it at
' the same time and only one of the update is passed through.
'
' To overcome the problem above, python provides a LOCK mechanism. This allows
' a thread to put a lock on a variable whenever a function wants to access
' that variable, so the variable is locked from the point of reference to the
' point of modification. Once the thread is done using the variable it unlocks
' it and another thread can now use that variable.
'''

# part of stdlib
import threading
from queue import Queue
import time # to mimic processing time

# creating a thread lock
print_lock = threading.Lock()

# defininf the job
def exampleJob(worker):
    time.sleep(0.5) # simulating computation time

    # Once the job is finished the "with" statement will release the lock
    with print_lock: # the print job won't run while print_lock is locked
        print(threading.current_thread().name, worker)

# does the actual threading opertation
def threader():
    while True:
        worker = q.get() # get the thread/worker from the queue
        exampleJob(worker) # run the worker through the job
        q.task_done() # then release the thread/worker back to the queue
        
'''
' Part1: Queue
'''
q = Queue()

'''
' Part2: Number of threads
'''
# creating threads, 10 in this case, these are the workers
for x in range(10):
    # defining a thread
    t = threading.Thread(target = threader)
    t.daemon = True # calssifing as a daemon, this thread dies with parent
    t.start() # start the thread

start = time.time() # starting time for performance calculations

'''
' Part3: Job assignment
'''
# creating 20 jobs and assigning them to workers
for worker in range(20):
    q.put(worker) # add the worker to the queue

# wait until thread terminates
q.join()

'''
' with 10 workers and 20 tasks, with each task being .5 seconds,
' then the completed job is ~1 second using threading.
' Normally 20 tasks with .5 seconds each would take 10 seconds.
'''
print("Entire job took:", time.time()-start)
