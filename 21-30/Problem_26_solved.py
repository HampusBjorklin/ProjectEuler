# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
# 2 to 10 are given:
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal
# fraction part.

from decimal import Decimal
from reused_functions import num_to_list


def find_repeating_decimal_length(num):
    decs = []
    nom = 1
    i = 1
    length = 0
    cycles = []
    while True:
        nom = nom * 10
        temp = nom // num
        decs.append(temp)
        nom = nom % num
        i += 1
        if i > num * 3:
            break
    flag = False

    for i in range(2, len(decs) // 2 + 1):
        for e in range(0, len(decs) - i):
            if decs[e:e + i] == decs[e + i:e + 2 * i] and decs[e:e + i] == decs[e + 2* i:e + 3 * i]:
                length = i
                flag = True
                break
        if flag:
            break
    return length

max_len = 0
ans = 0
d = 1000
while True:
    temp = find_repeating_decimal_length(d)
    if temp > max_len:
        max_len = temp
        ans = d
    if max_len > d:
        break
    d -= 1

print(ans, max_len)

