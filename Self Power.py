def self_powers(n):
    total = 0
    for i in range(1, n+1):
        total += i**i
    return total

n = 1000

erg = str(self_powers(n))[-10:]

print("Die letzten 10 Ziffern der Summe sind: ", erg)
