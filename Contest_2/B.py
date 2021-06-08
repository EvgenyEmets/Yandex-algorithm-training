c = int(input())
a = []
prob = 0
while c != -2000000000:
    a.append(c)
    c = int(input())
    if c != -2000000000 and prob != 6:
        if c == a[-1]: 
            if prob == 0:
                prob = 1
            elif prob == 2:
                prob = 3
            elif prob == 4:
                prob = 5
        elif c < a[-1]:
            if prob == 0:
                prob = 4
            elif prob == 1:
                prob = 5
            elif prob == 2 or prob == 3:
                prob = 6
        elif c > a[-1]:
            if prob == 0:
                prob = 2
            elif prob == 1:
                prob = 3
            elif prob == 4 or prob == 5:
                prob = 6
if prob == 1:
    print("CONSTANT")
elif prob == 2:
    print("ASCENDING")
elif prob == 3:
    print("WEAKLY ASCENDING")
elif prob == 4:
    print("DESCENDING")
elif prob == 5:
    print("WEAKLY DESCENDING")
else:
    print("RANDOM")
