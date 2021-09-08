from reused_functions import sieve_of_eratosthenes
import numpy as np
from math import sqrt

def is_prime(num):
    if num%2==0 or num < 1:
        return False
    for n in range(2, int(sqrt(num))+1):
        if num%n == 0:
            return False
    return True

b_primes_pos = sieve_of_eratosthenes(1000)
b_primes_neg = [x*-1 for x in b_primes_pos]
b_primes_neg.reverse()
b_primes = b_primes_neg + b_primes_pos
ans = 0
conf = []

for a in range(-999, 999, 2):
    for b in b_primes_pos:
        n = 0
        while True:
            print(np.polyval([1,a,b],n))
            if not is_prime(np.polyval([1,a,b],n)):
                print(n, [a,b])
                break
            n += 1
            if n > ans:
                ans = n
                conf = [a,b]
print(ans)
print(conf)