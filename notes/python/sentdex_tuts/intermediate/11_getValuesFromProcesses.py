# Getting values from multipcessing processes

'''
' Here we are using map() to get data back from a pool of processes but
' there are other ways to get data back from a process
'''

# Allows us to create a pool of process workers
from multiprocessing import Pool

def job(num):
    return num * 2


if __name__ == "__main__":
    p = Pool(processes=15) # using pool to create processes

    
    data = p.map(job, range(15)) # map the job to any iterable
    data2 = p.map(job, [5,2,6,7,8,9])

    p.close()

    print(data)
    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]    

    print(data2)
    # [10, 4, 12, 14, 16, 18]
