# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?
from reused_functions import factorize

def dividing_numbers(num):
    divsors = []
    for i in range(1,num//2+1):  # Only need to try from half of the and then add 1 later
        if num%i == 0:
            e = num/i
            if e < i:
                break
            if e == i:
                divsors.append(i)
            else:
                divsors.append(i)   # Each dividing number come in pairs, add both to list
                divsors.append(e)   # Stop when paired divisor is larger is smaller than i
    return divsors

tri_number = 28
i = 7
while True:
    i+=1
    tri_number += i
    if len(dividing_numbers(tri_number))>500:
        break
print(tri_number)
print()


print(dividing_numbers(12))