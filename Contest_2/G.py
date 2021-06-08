a = list(map(int, input().split()))
min1 = min(a[0], a[1])
min2 = max(a[0], a[1])
max1, max2 = min2, min1
for i in range(2, len(a)):
    if a[i] < min1:
        min1, min2 = a[i], min1
    elif a[i] < min2:
        min2 = a[i]
    if a[i] > max1:
        max1, max2 = a[i], max1
    elif a[i] > max2:
        max2 = a[i]
if max1*max2 > min1*min2:
    print(max2, max1)
else:
    print(min1, min2)
