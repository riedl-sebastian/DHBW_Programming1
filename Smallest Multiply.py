def kgT(n):
    def T(x):
        for i in range(1, n+1):
            if x % i != 0:
                return False
        return True

    x = n
    while not T(x):
        x += n
    return x

print(kgT(20))

# Project Euler Dreieckszahl:

def dreieck(n):
    return n * (n + 1) // 2

def fünfeck(n):
    return n * (3*n - 1) // 2

def sechseck(n):
    return n * (2*n - 1)

def euler_45():
    T = {dreieck(n) for n in range(286, 100000)}
    P = {fünfeck(n) for n in range(166, 100000)}
    H = {sechseck(n) for n in range(144, 100000)}

    return min(T & P & H)

print(euler_45())
