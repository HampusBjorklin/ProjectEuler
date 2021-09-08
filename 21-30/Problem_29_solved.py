list = []
for a in range(2,101):
    for b in range(2,101):
        power = a**b
        if power not in list:
            list.append(power)
    print(a)

print(len(list))