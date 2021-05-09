# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

from math import factorial
from reused_functions import num_to_list
num = factorial(100)
ans = 0
list = num_to_list(num)
for i in list:
    ans += int(i)

print(ans)
