# Problem 18 again, but with significantly larger triangle, bruteforce not an option.
# Pruning seem to be necessary this time
from reused_functions import minimax

f = open('tri.txt','r')
tri = f.read()
triangle = [list(map(int, x.split(' '))) for x in tri.splitlines()]
print(triangle)

print(minimax(triangle,0,0,99))
