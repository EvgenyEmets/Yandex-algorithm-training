a = int(input())
b = int(input())
n = int(input())
m = int(input())
min1 = (n-1)*a+n
max1 = min1 + 2*a
min2 = (m-1)*b+m
max2 = min2 + 2*b
if max(min1, min2) <= min(max1, max2):
	print(max(min1, min2), min(max1, max2))
else:
	print(-1)
