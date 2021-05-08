# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143?
import numpy as np

# Implement the Baillie-PSW primality test
small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

def lucas_sequence_U(n,P,Q):
    U = [0, 1]
    i = 2
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        while True:
            U_next = P * U[i-1] - Q * U[i-2]
            U.append(U_next)
            i += 1
            if i-1 == n:
                break
        return U[-1]

def lucas_sequence_V(n,P,Q):
    U = [2, P]
    i = 2
    if n == 0:
        return 2
    if n == 1:
        return P
    else:
        while True:
            U_next = P * U[i-1] - Q * U[i-2]
            U.append(U_next)
            i += 1
            if i-1 == n:
                break
        return U[-1]

def lucas_factorize(n):
    # Rewrite number n on form 2**s, where s >= 0 and d odd.
    ds = []
    i = 0
    while True:
        if n > 2**i:
            i += 1
        else:
            i -= 1
            break
    # This part only works for even numbers, but we already know than n is even so its fine.. fix later
    while True:
        d = (n / (2 ** i))
        if d%2 != 0 and d.is_integer():
            ds.append(int(d))
            break
        else:
            i-=1
        if i < 0:
            break
    ds.append(i)
    return ds

def is_prime(num):
    #Step 0. Check if num is even...
    if num%2 == 0:
        print('Step 0')
        return False
    # Step 1. perform trial division to test if num is divisible by any small prime
    for i in small_primes:
        if num%i == 0:
            print('Step 1')
            return False
    # Step 2. perform a base 2 strong probable prime test
    a = num - 1
    while True:
        if 2**a%num == 1 or 2**a%num == num -1:
            if a%2 == 0:
                break
            else:
                a = a/2
        else:
            print('Step 2')
            return False

    # Step 3. Find the first D in the sequence 5, -7, 9 , -11, 13, -15, ...  for which the jacobi symbol is -1
    # Set P = 1 and Q = (1-D)/4
    D = 5
    while True:
        if D%num != 0 and (np.sqrt(D%num)).is_integer():
            break
        else:
            if D > 0:
                D = -(D+2)
            else:
                D = -(D-2)

            if D > 50:
                print('ERROR: num maybe a perfect square...')
                break

    P = 1
    Q = (1-D)/4

    # Step 4. Perform a strong Lucas probable prime test on num using parameter D, P and Q.
    # If num is a strong Lucas probable prime, num is most likely a prime.

    delta_n = num + 1
    #if lucas_sequence_U(delta_n,P,Q)%num != 0:
       # print(lucas_sequence_U(delta_n,P,Q)%num)
       # print('Step 4.1')
       # return False

    ds = lucas_factorize(delta_n)
    d = ds[0]
    s = ds[1]
    print(d,s)
    U_d = lucas_sequence_U(d, P, Q)
    if U_d%num == 0:
        print('Step 4')
        return True
    
    for i in np.arange(0,s+1)[:-1]:
        x = d * 2 ** i
        V_x = lucas_sequence_V(x, P, Q)
        print(V_x%num)
        if V_x % num == 0:
            print('Step 4.1')
            return True

    else:
        print('Step 4.2')
        return False

print(is_prime(29))
