def h_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nice_prime(n):
    str_n = str(n)
    return all(h_prime(int(str_n[i:] + str_n[:i])) for i in range(len(str_n)))

circular_primes = [n for n in range(2, 1000000) if nice_prime(n)]

print("Zirkuläre Primzahlen unter 1.000.000:", circular_primes)
print("Anzahl der zirkulären Primzahlen unter 1.000.000:", len(circular_primes))
