def maxPrice_rec(dyn,arr,size,start):
    if size==start:
        print(dyn)
        """
        Every element is the max price 
        that can be sold for (index+1) cm candy
        """
        return dyn[size-1]
    maxprice = 0
    for j in range(0,start+1):
        maxprice=max(maxprice,arr[j]+dyn[start-j-1])
    dyn[start]=maxprice
    return maxPrice_rec(dyn, arr, size, start+1)

def maxPrice(arr, size):
    dyn = [0 for x in range(len(arr))]
    dyn[0] = arr[0]
    return maxPrice_rec(dyn,arr, size, 0)
prices = [1, 5, 8, 9, 10, 17, 17, 20]
size=8
max = maxPrice(prices,size)
print("Maximum Price is: " + str(max))
