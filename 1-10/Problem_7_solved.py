# By listing the first six prime numbers: 2,3,5,7,11,13 we can see that the 6th prime is 13.
# What is the 10 001th prime number?
import numpy as np

known_primes = [2, 3, 5, 7, 11, 13]
i = 15

while len(known_primes)<10001:
    # Check if prime is divisible by any of the known primes...
    divisible = False
    for n in known_primes:
        if i%n == 0:
            divisible = True
            break

    if not divisible:
        for n in range(15, int(np.sqrt(i)+1)):
            if i%n == 0:
                divisible = True
                break

    if not divisible:
        known_primes.append(i)

    # Increment 2 since we only has to test odd numbers
    i += 2

print(known_primes[-1])




