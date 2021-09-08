import math
def minimax(tri, row, index , depth):
    if depth == 0:
        return tri[row][index]
    # No need for minimizing player...
    maxeval = -math.inf
    for i in range(2):
        eval = tri[row][index] + minimax(tri, row+1, index+i, depth-1)  # Sum best option with current position
        maxeval = max(maxeval, eval)
    return maxeval


def dividing_numbers(num):
    divsors = []
    for i in range(1,num//2+1):  # Only need to try from half of the and then add 1 later
        if num%i == 0:
            e = num/i
            if e < i:
                break
            if e == i:
                divsors.append(i)
            else:
                divsors.append(i)   # Each dividing number come in pairs, add both to list
                divsors.append(e)   # Stop when paired divisor is larger is smaller than i
    return divsors