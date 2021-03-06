# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting
# with 1 and 2, the first terms will be: 1,2,3,5,8,13,21,34,55,89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
# even-valued terms.

first_fib = 1
second_fib = 2
even_fibs = []
done = False
while True:
    next_fib = first_fib + second_fib
    first_fib = second_fib
    second_fib = next_fib
    if next_fib >= 4*10**6:
        break
    if next_fib % 2 == 0:
        even_fibs.append(next_fib)
ans = sum(even_fibs) + 2
print(ans)