# A palindromic number read the same both ways. The largest palindrome made from the product of two
# 2-digit numbers is 9009 = 91 * 99
# Find the largest palindrome made from the product of two 3-digit numbers.

import numpy as np
from Problem_3_solved import find_largest_prime

def num_to_list(num):
    num_list = []
    num_str = str(num)
    for i in num_str:
        num_list.append(i)
    return num_list

def decrement_list(list):
    list_int = int(''.join(list))
    list_int -= 1
    dec_list = num_to_list(list_int)
    return dec_list

def increment_list(list):
    list_int = int(''.join(list))
    list_int += 1
    inc_list = num_to_list(list_int)
    return inc_list


def generate_next_pal(num):
    # Given a palindrome, return the next (lower) palindrome
    # If given number is not a palindrome, return closest palindrome
    num_list = num_to_list(num)

    if len(num_list)%2 == 0:
        middle = int(len(num_list)/2)
        first_half = num_list[0:middle]
        second_half = num_list[middle:]
        second_half.reverse()

        if first_half != second_half:
            first_half.reverse()
            num_list[middle:] = first_half

        else:
            len1 = len(num_list)
            first_half = decrement_list(first_half)
            num_list[:middle] = first_half
            first_half.reverse()
            num_list[middle:] = first_half
            len2 = len(num_list)
            if len1 != len2:
                num_list = ['9']*len2

    else:
        middle = int(len(num_list)//2)+1
        first_half = num_list[0:middle]
        second_half = num_list[middle:]
        second_half.reverse()

        if first_half[:-1] != second_half:
            first_half.reverse()
            num_list[middle:] = first_half[1:]

        else:
            len1 = len(num_list)
            first_half = decrement_list(first_half)
            second_half = first_half[:-1]
            second_half.reverse()
            num_list = first_half + second_half
            len2 = len(num_list)
            if len1 != len2:
                num_list = ['9']*(len1-1)

    num_str = ''.join(num_list)
    palindrome = int(num_str)
    return palindrome

# Create list of all palindromes smaller then the limit
'''
limit = 999999
palindromes = []
while True:
    limit = generate_next_pal(limit)
    palindromes.append(limit)
    # Dont need the smaller ones since we know they can be created with 2 digits...
    if limit < 1000:
        break

done = False
for n in palindromes:
    for i in reversed(range(1,1000)):
        if n%i == 0 and n/i < 1000:
            print(n,i, n/i)
            done = True
            break
    if done:
        break
'''







