import numpy as np

def dividing_numbers(num):  # Slightly changed from last use...
    divsors = []
    for i in range(1,num//2+1):  # Only need to try from half of the and then add 1 later
        if num%i == 0:
            e = num/i
            if e < i:
                break
            if e == i or i == 1: # Changed so input num not in list
                divsors.append(int(i))
            else:
                divsors.append(int(i))   # Each dividing number come in pairs, add both to list
                divsors.append(int(e))   # Stop when paired divisor is larger is smaller than i
    return divsors


def num_to_list(num):
    num_list = []
    num_str = str(num)
    for i in num_str:
        num_list.append(i)
    return num_list


def find_largest_prime(num):
    if num == 1:
        return 1
    i = 2
    while True:
        if num%i == 0:
            if i == num:
                return i
            else:
                num = num/i
                i = 2
        else:
            i += 1


def factorize(num):
    factors = []
    temp = num
    while True:
        temp = find_largest_prime(num)
        num = num/temp
        factors.append(temp)
        if num == 1:
            break
    return factors


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

