def max_profit_rec(regs,start,maxN):
    if start==len(regs):
        return maxN 
    for j in range(len(regs)-1,-1,-1):
        possibleMax = max(regs[j]-regs[start], regs[j])
        if maxN<possibleMax:
            maxN = possibleMax
    return max_profit_rec(regs, start+1, maxN)

def max_profit(arr):
    for i in range(1,len(arr)):
        arr[i]=arr[i]+arr[i-1]
    return max_profit_rec(arr,0,0)

regions = [ 3, -5, 2, 11, -8, 9,-5]
maxPro=max_profit(regions)
print("Max profit: "+str(maxPro))
