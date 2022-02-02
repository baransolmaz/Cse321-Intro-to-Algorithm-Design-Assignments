def brute(a,n):
    res=1
    for i in range(0,n):
        res=res*a
    return res
def divide(a,n):
    if (n==1):
        return a
    mid=int(n/2)
    return divide(a,mid)*divide(a,n-mid)
    
a=5    
n=8
b=brute(a,n)
d=divide(a,n)
print("Brute:"+str(b))
print("Divide:"+str(d))