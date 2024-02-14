# Summe der Primzahlen unter 1000000
import time

start_time=time.time()

n = 1000000
i=0
z=1
s=0
while i<=n:
    while z<=50:
        while s<n:
            if i%z!=0:
                s=s+i
    z=z+1
    i=i+1
    print(s)
            
end_time=time.time()

zeit=end_time-start_time()
print(start_time)
print(end_time)
print(zeit)
