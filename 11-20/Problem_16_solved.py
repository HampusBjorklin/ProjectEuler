# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
from reused_functions import num_to_list

num = 2**1000
list = num_to_list(num)
ans = 0
for i in list:
    ans += int(i)

print(ans)
