def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-2)+fibo(n-1)

a= fibo(7)
print(a)
 #its complexity is 2 power n ..it is bad fibonacci