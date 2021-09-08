n = 3
upper_diag = 0
lower_diag = 0
while True:
    sqr = n*n
    print(sqr)
    upper_diag += sqr
    lower_diag += sqr - (n-1)*3
    n+=2
    if n > 1001:
        break

print(upper_diag, lower_diag)
print(2*(upper_diag + lower_diag) + 1)