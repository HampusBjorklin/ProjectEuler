# The sum of the squares of the first ten natural numbers is, 1**2 + 2**2 + 3**2 ... + 10**2 = 385
# The square of the sum of the natural numbers is, (1 + 2 + 3...+ 10)**2 = 3025
# Hence the difference between the sum of the squares of the ten natural numbers and the square sum is
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import numpy as np

def find_square_difference(n):
    series = np.arange(1,n+1)
    squared_series = sum(series**2)
    square_sum = sum(series)**2
    difference = square_sum - squared_series
    return difference


print(find_square_difference(100))