from reused_functions import num_to_list

num = 2**1000
list = num_to_list(num)
ans = 0
for i in list:
    ans += int(i)

print(ans)
