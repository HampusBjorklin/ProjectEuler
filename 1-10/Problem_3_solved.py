# The prime factors of 13195 are 5,7,13,and 29
# What is the largest prime factor of the number 600851475143
import numpy as np
def find_largest_prime(num):
    if num == 1:
        return 1
    i = 2
    while True:
        if num%i == 0:
            if i == num:
                return i
            else:
                num = num/i
                i = 2
        else:
            i += 1

# num = 600851475143
# print(find_largest_prime(num))
