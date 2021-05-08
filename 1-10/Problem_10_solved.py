# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Cannot reuse code from problem 7, too slow for generating this many primes.
import numpy as np

#Use sieve of eratosthenes to find all primes below 2 million
def sieve_of_eratosthenes(limit):
    primes_list = []
    limit_range = [True]*(limit-1)

    for i in range(len(np.sqrt(limit_range)+1)):
        i += 2
        if limit_range[i-2]:
            j = i ** 2
            while j < limit+1:
                limit_range[j-2] = False
                j += i


    for n in range(len(limit_range)):
        n += 2
        if limit_range[n-2]:
            primes_list.append(n)
    return primes_list

print(sum(sieve_of_eratosthenes(2000000)))

