# Project Euler Problem 16

def summe():
    num = 2 ** 1000
    return sum(int(digit) for digit in str(num))

print(summe())
