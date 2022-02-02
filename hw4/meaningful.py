def decrease(arr,k):
    min=arr[0]
    index=0
    for i in range(0,len(arr)):
        if min>arr[i]:
            min=arr[i]
            index=i
    if k==1:
        return min
    arr.pop(index)
    return decrease(arr,k-1)

rates = [5, 3, 9, 6, 7, 50, 9, 0, 1, 5, 4, 45, 12, 8]
n=2
nth = decrease(rates,n)
print("nth: "+str(nth))  
