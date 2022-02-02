def mergeSortV2(myList):
    counter=0
    if len(myList) > 1:
        mid = int(len(myList) / 2)
        left = myList[:mid]
        right = myList[mid:]

        counter += mergeSortV2(left)
        counter += mergeSortV2(right)
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                counter+=(len(left)-i)
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
    return counter

pairs = [48, 3, 4, 6, 1, 15, 9, 10]

num = mergeSortV2(pairs)
print("Number of Reverse Pairs:"+str(num))
