def is_pandigital(n, s=9): 
    n=str(n)
    return len(n)==s and not '1234567890'[:s].strip(n)

def concatenated_product(j, n):
    return int(''.join(str(j*i) for i in range(1, n+1)))

max_val = 0
for i in range(1, 10000):
    for n in range(1, 10):
        val = concatenated_product(i, n)
        if is_pandigital(val):
            max_val = max(val, max_val)

print(max_val)
