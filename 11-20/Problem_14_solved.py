# Collatz conjecture...
# Which number under 1 million produces the longest chain before arriving at 1.

def collatz_chain(num, dict):
    count = 0
    while num != 1:
        if num in dict:
            count += dict[num]      # If number which we know convergence-length appears we don't need to keep
            break                       # computing...
        if num % 2 == 0:
            num = num/2
            count += 1
        else:
            num = (3*num + 1)/2  # Slight efficiency increase by noting that all odd numbers multiplied by 3
            count += 2              # and incremented by one results in even number

    return count

dict = {}
max_len = 0
max_n = 0
for i in range(int(1e6+1), 1, -1):
    length = collatz_chain(i, dict)
    if length > max_len:
        max_len = length
        max_n = i
    dict[i] = length

print(max_n)

