from math import sqrt, floor

def divisors(n):
    return list(filter(lambda i: n % i == 0, range(1, n+1)))

print(divisors(172))
