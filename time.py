import time
start=time.time()
print(start)
s=0
n=int(input())
for i in range(n+1):
	s=s+(2**i)
end=time.time()
print(end-start)
print(str(end-start) +'secs')
print(s)