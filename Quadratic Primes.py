import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def quadratic_primes():
    max_n = 0
    product = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(n * n + a * n + b):
                n += 1
            if n > max_n:
                max_n = n
                product = a * b
    return product

print(quadratic_primes())
