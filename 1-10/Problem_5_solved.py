# 2520 is the smallest number that can be divided by each of the numbers 1 to 10 without
# any remainder. What is the smallest number than can be divided by all number 1 to 20?
from Problem_3_solved import find_largest_prime
import numpy as np
from collections import Counter

# Find all prime factors as a list of a given numbers
def factorize(num):
    factors = []
    temp = num
    while True:
        temp = find_largest_prime(num)
        num = num/temp
        factors.append(temp)
        if num == 1:
            break
    return factors

# For all numbers 1 to 20, factorize.
nums = np.arange(2,21)
factors = []
for n in nums:
    fact = factorize(n)
    factors.append(fact)

# Reverse list
factors.reverse()

# Start from 20, append factors to list, if factors already exist in list, don't att duplicates
factors_set = []
for i in factors:
    intersect = list((Counter(i) & Counter(factors_set)).elements())
    for n in intersect:
        i.remove(n)
    factors_set += i

ans = np.prod(factors_set)
print('Smallest divisible number: ' + str(ans)+ '\n dividing...')

for i in nums:
    print(i, ans/i)






