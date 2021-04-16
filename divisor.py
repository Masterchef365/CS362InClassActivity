from math import sqrt, floor

def divisors(n):
    return list(filter(lambda i: n % i == 0, range(1, n+1)))

print(divisors(int(input("Enter a number to find divisors: "))))
