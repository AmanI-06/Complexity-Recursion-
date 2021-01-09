from time import time 
def comput(n):
    data=[]
    start=time()
    for j in range(n):
        data.append(None)
    end=time()
    return(end-start)/n

a=comput(100000)  #the time elapsed between the start and end includes the time to manage the iteration of the for loop, in addition to the append call
print(a)