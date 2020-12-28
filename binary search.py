def bsearch(l,key,low,high):
    
    if low<=high:
        mid=(low+high)//2
        if key==l[mid]:
            return mid
        elif l[mid]<key:
            return bsearch(l,key,mid+1,high)
        else:
            return bsearch(l,key,low,mid-1)
    else :
        print("u dumfuk see ur typo")
     

l=[2,4,5,6,78,89]
a=bsearch(l,5,1,len(l)+1)
print(a)