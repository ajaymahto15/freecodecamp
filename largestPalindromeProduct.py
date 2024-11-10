# Problem 4: Largest palindrome product
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two n-digit numbers.
# 
# Run the Tests (Ctrl + Enter)
# Reset this lesson
# Get Help
# Tests
# Waiting:1. largestPalindromeProduct(2) should return a number.
# Waiting:2. largestPalindromeProduct(2) should return 9009.
# Waiting:3. largestPalindromeProduct(3) should return 906609.
# 
# Algo:
# 1. Find the largest n-digit number. (nLargest)
# 2. Loop backwards (nLargest-1) and get products with nLargest.
# 3. At each step of the loop check if the product is palindrome.
# 4. For palindrome check -
#    - Change number to string format 
#    - Compare till the mid of the string.
#    - If all characters are same, then return palindrome else not palindrome

import time


def isPalindrome(n):
    nStr = str(n)
    i, j = 0, len(nStr)-1
    flag = 0
    while (i < j):
        if nStr[i] != nStr[j]:
            flag = 1
            break
        i += 1
        j -= 1
    return (flag == 0)

def nDigitLargest(n):
    nLargest = ""
    for i in range(0,n):
        nLargest += '9'
    return int(nLargest)

def main():
    n = int(input())
    lNum = nDigitLargest(n)
    sNum = pow(10, n-1)
    globalMax = 1
    for i in range(lNum, sNum, -1):
        localMax = 1
        for j in range(lNum, sNum, -1):
            product = i*j
            #time.sleep(0.05)
            print("Multiplying: %s * %s = %s" % (str(i), str(j), str(product)))
            if isPalindrome(product):
                localMax = product
                break
        print("localMax for %s -- %s", (str(i), str(localMax)))
        #time.sleep(0.2)
        if localMax > globalMax:
            print("localMax greater than globalMax -- changing..")
            globalMax = localMax
            #time.sleep(0.2)
    print(globalMax)

if __name__ == '__main__':
    main()