# Multiprocessing with python

'''
' Multiprocessing is a built-in library.
' Python is a single core language by default, which has performance impact
' This handicap is beacuse of something called GIL (Global Interpreter Lock)
' it was initially put in place as a memory management safegaurd, though today
' we have better idea nowdays, we can't simply take out the GIL beacuse there is
' a lot of infrastructure built with the assumption that we have GIL's
' memory management safegaurd in place. So it is here to stay and hence the
' need for a multiprocessing library
'
' In a 4 core processor a single python program/process will only utilise 25%
' of processing capacity i.e use only one CPU core, if we launch the same
' program again it will launch in another CPU core now technically utilising
' 50% of processing power, so and so forth. The programs don't talk to
' each other.
'
' The multiprocessing library allows us to launch seperate python processes,
' these processes don't necessarly talk to each other or pass values between
' them but the library makes it easy for us to do so, without us needing
' to write custom pipes if we were manually running seperate programs
'''

### NOTE: tested on an Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz ###
import multiprocessing

def spawn(num):
    print("Spawned! {}".format(num))

#### RUN in terminal to see the output ####
    
# Necessary in multiprocessing
if __name__ == "__main__":
    for i in range(10000): # 5 processes
        # when passing a single argument we need to end with a comma
        p = multiprocessing.Process(target=spawn, args=(i,)) # spawn a process
        p.start() # start process
        
        '''
        ' join() blocks until the process whose join() method is called
        ' terminates, so the processes execute in order
        ' this is slightly slow as it doesn't max out each core
        ' being less resource hungry [~ 36-40% CPU (core) usage]
        ' If we remove the join the processes will be faster and execute out of
        ' order and utilise the CPU cores extensively
        ' [~ 98-100% CPU (core) usage]
        '
        ' join() also becomes important when sharing data between process, like
        ' waiting on a variable to be updated or passed
        '''
        p.join() # wait for the process to be completeted

