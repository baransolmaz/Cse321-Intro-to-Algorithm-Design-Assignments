def maxCourse(start_index,starts,ends,count,maximum):
    
    if ends[start_index]>=max(starts):
        return count+1
    for i in range(0,len(ends)):
        if ends[start_index]<=starts[i]:
            newMax=maxCourse(i,starts,ends,count+1,maximum)
            maximum=max(newMax,maximum)
    return maximum


starts=[1,3,0,5,8,5]
ends  =[2,4,6,7,9,9]
maxC=0
for i in range(0,len(ends)):
    newmax=maxCourse(i,starts,ends,0,maxC)
    maxC = max(newmax, maxC)
print("Max Number of Courses: "+str(maxC))
