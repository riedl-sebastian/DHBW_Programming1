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
