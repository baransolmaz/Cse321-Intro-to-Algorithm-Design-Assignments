def cut(size):
    if size==1:
        return 0
    return cut(int(size/2)+(size%2))+1
    
   
size=16
count=cut(size)
print("Number of cuts: "+str(count))
