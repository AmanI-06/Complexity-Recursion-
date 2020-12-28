def avg3(s):
    n=len(s)
    a=[0]*n
    tot=0
    for i in range(n):
        tot+=s[i]    # o(N)
        av=tot/n
    return av

v=avg3([1,2,3])
print(v)