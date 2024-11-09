# Problem 1: Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
# 
# Run the Tests (Ctrl + Enter)
# Reset this lesson
# Get Help
# Tests
# Waiting:1. multiplesOf3Or5(10) should return a number.
# Waiting:2. multiplesOf3Or5(49) should return 543.
# Waiting:3. multiplesOf3Or5(1000) should return 233168.
# Waiting:4. multiplesOf3Or5(8456) should return 16687353.
# Waiting:5. multiplesOf3Or5(19564) should return 89301183.

def main():
    n = int(input())
    sum = 0
    for i in range(0, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)
if __name__ == '__main__':
    main()