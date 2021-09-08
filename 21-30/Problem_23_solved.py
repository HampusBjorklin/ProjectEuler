# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
# exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of
# two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that
# the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from reused_functions import dividing_numbers
import math


def abundant(num):
    if num < sum(dividing_numbers(num)):
        return True
    else:
        return False

def is_sum(num,list):
    for i in list:
        e = 1
        while True:
            temp = num - e*i
            if temp < 1:
                break
            for n in list:
                if temp%n == 0:
                    return True
            e+=1
    return False


abundant_nums = []
for n in range(1, 28124):
    flag = True
    '''for i in abundant_nums:
        if n%i == 0:
            flag = False
            break
    if flag:'''
    if abundant(n):
        abundant_nums.append(n)

abundant_sums = []
for n in abundant_nums:
    for i in abundant_nums:
        temp = n + i
        if temp < 28123:
            abundant_sums.append(temp)

ans = sum(range(28123)) - sum(set(abundant_sums))
print(ans)