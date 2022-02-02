import math
def min_distance(space):
    min= 999
    sum=0
    pairs=[]
    for i in range(0,len(space)):
        for j in range(i+1, len(space)):
            for k in range(0,len(space[0])):
                sum += ((space[i][k]-space[j][k])**2)
            dist=math.sqrt(sum)
            if dist<min:
                pairs.clear()
                min=dist
                pairs.append(space[i])
                pairs.append(space[j])
            sum=0
    
    return min ,pairs


space = [(1,2,2), (0, 0,0),(5,5,5)]
#space=[(1,2),(4,5),(12,5),(6,9),(45,45),(0,0),(8,8),(70,3)]
min, pair =min_distance(space)
print(pair)
print("Distance: " +str(min))
