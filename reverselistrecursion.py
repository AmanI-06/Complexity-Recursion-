def rev(s,n):
    for i in range(len(s),1,-1):
        return s[i]
    
if __name__=="__main__":
    n=(int(input()))
    s=list(map(int,input("enter list").split(',')))
    a=rev(s,n)
    print(a)