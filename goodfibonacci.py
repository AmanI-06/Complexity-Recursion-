def gfibo(n):
    if n<=1:
        return(n,0)
    else:
        (a,b)=gfibo(n-1)
        return a+b,a

a=gfibo(3)
print(a)