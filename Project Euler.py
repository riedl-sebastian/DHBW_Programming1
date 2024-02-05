# Multiples of 3 and 5 sum

n=1000
i=0
z=0
while i<n:
    if i%3==0 or i%5==0:
        z = z+i
        print(i)
    else:
        print(i," ist nicht durch 3 oder 5 teilbar")
    i=i+1
print(z)