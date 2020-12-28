def avg2(s):
    n=len(s)
    a=[0]*n
    for j in range(n):
        a[j]=sum(s[0:j+1])/(j+1)    # takes 1+2+...n iterations so o(n^2)
    return a[j]

v=avg2([1,2,3])
print(v)
