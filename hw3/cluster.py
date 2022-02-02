def most_profitable (regs):
    most=[]
    max=0
    for i in range(0,len(regs)):
        sum = 0
        for j in range(i,len(regs)):            
            sum+= regs[j][1]
            if sum > max:
                most= regs[i:j+1]
                max=sum
    return most      


def max_profit(arr):
    if len(arr)==1:
        return arr[0][1]
    index=int(len(arr)/2)
    left=max_profit(arr[0:index])
    rigth = max_profit(arr[index:None])
    return left+rigth
        

regions = [("A", 3), ("B", -5), ("C", 2), ("D", 11),
           ("E", -8), ("F", 9), ("G", -5)]
most = most_profitable(regions)
max= max_profit(most)
m = ""
for i in most:
    m += i[0]
print("Most Profitable Region: "+m)
print("Max Profit: "+ str(max))
