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