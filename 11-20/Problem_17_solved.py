# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?

singles = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
           'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
           'nineteen']

tens = ['', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
length = 0

for c in singles[0:10]:
    if c == '':
        for d in tens:
            if d == '':
                for i in singles:
                    print(i)
                    length += len(i)
            else:
                for i in singles[:10]:
                    print(d+i)
                    length += len(d+i)
    else:
        for d in tens:
            if d == '':
                for i in singles:
                    if i == '':
                        print(c+'hundred')
                        length += len(c+'hundred')
                    else:
                        print(c+'hundredand'+i)
                        length += len(c+'hundredand'+i)
            else:
                for i in singles[:10]:
                    print(c+'hundredand'+d+i)
                    length += len(c+'hundredand'+d+i)

print('onethousand')
length += len('onethousand')

print(length)