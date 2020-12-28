def avg(s):
    n=len(s)
    a=[0]*n
    for i in range(n):  #o(n)
        tot=0   #o(n)
        for j in range(i+1):   #1+2+3...+n  so n(n+1+/2 ) ~o(n^2)
            tot+=s[j]
        a[j]=tot/(j+1)
    return tot
    
b=avg([1,2,3,4,5,5])
print(b)
