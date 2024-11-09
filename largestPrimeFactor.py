# Problem 3: Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the given number?
# 
# Run the Tests (Ctrl + Enter)
# Reset this lesson
# Get Help
# Tests
# Waiting:1. largestPrimeFactor(2) should return a number.
# Waiting:2. largestPrimeFactor(2) should return 2.
# Waiting:3. largestPrimeFactor(3) should return 3.
# Waiting:4. largestPrimeFactor(5) should return 5.
# Waiting:5. largestPrimeFactor(7) should return 7.
# Waiting:6. largestPrimeFactor(8) should return 2.
# Waiting:7. largestPrimeFactor(13195) should return 29.
# Waiting:8. largestPrimeFactor(600851475143) should return 6857.

def isPrime(n):
    factor_count = 0
    for i in range(2, n):
        if n % i == 0:
            factor_count += 1
    return (factor_count == 0)
def main():
    n = int(input())
    maxPrime = 1
    for i in range(1, n+1):
        if n % i == 0 and isPrime(i):
            maxPrime = i
    print(maxPrime)
if __name__ == '__main__':
    main()