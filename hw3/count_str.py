def count_str(str,first,last):
    count=0;
    for i in range(0, len(str)):
        if(str[i]==first):
            for j in range(i+1, len(str)):
                if(str[j]==last):
                    count=count+1
    return count

#  Driver Code
myStr = 'TXZXXJZWX'
count=count_str(myStr,'X','Z')
print("Number of Substrings: " + str(count))