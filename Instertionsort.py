

def sortieren(array):
    for i in range(1,len(array)):
        m=array[i]
        j=i-1
        while j>=0 and m<array[j]:
            array[j+1]=array[j]
            j =j-1
            array[j+1]=m
            return array
        
s=[1,8,13,2,5,3,89,65436,256,345,566,234,77,2,6765,4,7,23,76,7]
print(sortieren(s))
