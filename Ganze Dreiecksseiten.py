from math import sqrt

Moegliche = {}

for a in range(1, 1000):
    for b in range(1, int(a / 2) + 1):
        c = sqrt(a ** 2 + b ** 2)
        Umfang = a + b + c
        if c == int(c) and Umfang < 1001:
            Moegliche[Umfang] = Moegliche.get(Umfang, 0) + 1

inverse = [(value, key) for key, value in Moegliche.items()]
print(max(inverse)[1])
