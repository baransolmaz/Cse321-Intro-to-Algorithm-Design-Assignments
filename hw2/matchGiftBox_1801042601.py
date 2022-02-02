class main :
    def partition(self, arr,  low,  high,  pivot) :
        i = (low - 1)
        j = low
        while (j <= high - 1) :
            if (arr[j] <= pivot) :
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return  (i + 1)
    
    def sort(self, gifts,  boxes,i) :
        if(i>= len(gifts)):
            return
        self.partition(boxes, 0, len(boxes) - 1, gifts[i])
        self.sort(gifts,boxes,i+1)
            
    #  Driver Code
    def main(self, args) :
        boxes = [5, 3, 4, 6, 7, 1, 2]
        gifts = [2, 3, 4, 5, 6, 7, 1]
        self.sort(gifts, boxes,0)
        self.sort(boxes, gifts,0)
        
        print("Gifts array: ",gifts)
        print("Boxes array: ",boxes)



if __name__=="__main__":
    main().main([])