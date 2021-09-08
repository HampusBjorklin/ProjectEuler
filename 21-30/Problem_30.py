# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def sum_of_fifth_powers(num):   # Func testing if sum digits raised to five equal input
    num_list = []
    temp = num
    while True:
        num_list.append(temp%10)       # Split digit into list
        temp = temp // 10
        if temp < 1:
            break
    sum_of_powers = sum([n**5 for n in num_list])   # Check if equal to input
    return sum_of_powers == num

i = 2
solutions = []
while True:
    if sum_of_fifth_powers(i):
        solutions.append(i)
        print(i)
    i += 1
    if i > 354294:  # 9^5 = 59049, the maximum sum for a 7 digit sum < 1e6
        break       # Thus 6 * 59049 is our upper limit for searching
print(sum(solutions))

