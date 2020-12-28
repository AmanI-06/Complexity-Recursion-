def linear(s,n):
    if n==0:
        return 0
    else:
        return linear(s,n-1) +s[n-1]

if __name__=="__main__":
    n=(int(input()))
    s = list(map(int,input("\nEnter the numbers : ").split(',')))
    a=linear(s,n)
    print(a)


    s=list(map(int,input))