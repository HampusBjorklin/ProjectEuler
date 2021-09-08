# Using names.txt (right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list
# to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?
import string

def wordsplit(word):
    return [char for char in word]


f = open('names.txt','r')
str = f.read().replace('"','')
f.close()
lst = str.split(',')
lst.sort()
totscore = 0
for n, name in enumerate(lst):
    n += 1
    score = 0
    for i in wordsplit(name):
        score += string.ascii_uppercase.index(i) + 1
    score = score*n
    totscore += score
print(totscore)
