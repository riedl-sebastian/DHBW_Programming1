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

# Noch ein Problem
def abundant(n):
    factors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)
    return sum(factors) - n > n

abundant_numbers = [i for i in range(1, 28124) if abundant(i)]
abundant_sums = {i+j for i in abundant_numbers for j in abundant_numbers if i+j < 28124}

all_numbers = set(range(1, 28124))
non_abundant_sums = all_numbers - abundant_sums

print(sum(non_abundant_sums))
