# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
i = 2
F = 1
temp = 1
while True:
    mem = F
    F = F + temp
    temp = mem
    i += 1
    if F > 10**999:
        print(i)
        break
