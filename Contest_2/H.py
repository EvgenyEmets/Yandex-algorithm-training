a = list(map(int, input().split()))
min1 = min(a[0], a[1], a[2])
min3 = max(a[0], a[1], a[2])
min2 = a[0] + a[1] + a[2] - min1 - min3
max1, max2, max3 = min3, min2, min1
for i in range(3, len(a)):
    if a[i] < min1:
        min1, min2, min3 = a[i], min1, min2
    elif a[i] < min2:
        min2, min3 = a[i], min2
    elif a[i] < min3:
        min3 = a[i]
    if a[i] > max1:
        max1, max2, max3 = a[i], max1, max2
    elif a[i] > max2:
        max2, max3 = a[i], max2
    elif a[i] > max3:
        max3 = a[i]
if max1*max2*max3 > min1*min2*max1:
    print(max3, max2, max1)
else:
    print(min1, min2, max1)
