def MaxCheese(weights, prices, capacity):
    data = []
    for i in range(len(weights)):
        data.append([weights[i], prices[i]])
    data.sort(reverse=True,key= lambda x:(x[1]//x[0]))
    totalPrice = 0.0
    for cheese in data:
        currentWeight = cheese[0]
        currentValue = cheese[1]
        if capacity - currentWeight >= 0:
            capacity -= currentWeight
            totalPrice += currentValue
        else:
            unitPrice = currentValue / currentWeight
            totalPrice += capacity * unitPrice
            capacity = capacity - (currentWeight * unitPrice)
            break
    return totalPrice                       

weights = [6, 3, 2, 8]
prices = [36,15,20,32]
capacity = 10

maxValue = MaxCheese(weights, prices, capacity)
print("Maximum value in cheese =", maxValue)
