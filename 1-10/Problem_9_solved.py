# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a**2 + b**2 = c**2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Euclids formula for generating a pythagorian triple from integers m>n>0
# a = m**2 - n**2, b = 2mn, c = m**2 + n**2

# From this; m**2 - n**2 + 2mn + m**2 + n**2 = 1000
# => 2(m**2) + 2mn = 1000

# Find integer solution, not trivial solutions with a, b = 0
import numpy as np
done = False
n = 0
while not done:
    n+=1
    ans = 0
    m = n + 1
    while ans < 1000 and not done:
        ans = m**2 - n**2 + 2*m*n + m**2 + n**2
        if ans == 1000:
            done = True
        else:
            m += 1

a = m**2 - n**2
b = 2*m*n
c = m**2 + n**2

print(a,b,c)
print('sum: ' + str(a+b+c))
print('product: ' + str(a*b*c))



