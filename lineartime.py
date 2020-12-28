
def max(data):
    b=data[0]
    for i in data:
        if i>b:   #o(n)
            b=i
    return b

f=[1,3,4,6,78,99]
v=max(f)
print(v)