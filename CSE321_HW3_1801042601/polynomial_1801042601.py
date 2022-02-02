def func(arr,x):
    result=0
    for i in range(0,len(arr)):
        result += (arr[len(arr)-1-i]*(x**i))
    return result

arr=[1,2,3,4]#kat sayılar x^3 + 2x^2 + 3x + 4    
print(func(arr,2))    
