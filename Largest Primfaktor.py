def b_prim(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

zahl = 100
print("Der größte Primfaktor von", zahl, "ist", b_prim(zahl))
