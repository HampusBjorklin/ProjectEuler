# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# the sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import numpy as np
limit = 1000
three_floor = (limit-1)//3 # Floor division. Get highest int that when multiplied with 3 is less than limit
fives_floor = (limit-1)//5
threes = 3*np.arange(1, three_floor + 1)
fives = 5*np.arange(1, fives_floor + 1)
union = np.union1d(threes,fives) # Don't count numbers which are divisible both by 3 and 5 twice...
ans = sum(union)
print(ans)