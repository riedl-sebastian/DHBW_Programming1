# Project Euler Problem 29
distinct_terms = set(a**b for a in range(2, 101) for b in range(2, 101))
print(len(distinct_terms))
