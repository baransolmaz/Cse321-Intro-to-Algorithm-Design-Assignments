def divide_best(rates):
    if len(rates)==1:
        return rates[0]
    mid=int(len(rates)/2)
    in1=divide_best(rates[0:mid])
    in2 = divide_best(rates[mid:len(rates)])
    if in1>in2:
        return in1
    else:
        return in2

def divide_worst(rates):
    if len(rates) == 1:
        return rates[0]
    mid = int(len(rates)/2)
    in1 = divide_worst(rates[0:mid])
    in2 = divide_worst(rates[mid:len(rates)])
    if in1 < in2:
        return in1
    else:
        return in2

rates= 5,3,9,6,7,50,9,0,1,5,4,45,12,8
best=divide_best(rates)
worst = divide_worst(rates)
print("Best: "+str(best))
print("Worst: "+str(worst))
