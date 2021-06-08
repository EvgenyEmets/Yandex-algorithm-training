a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
m1 = min(a, b, c)
m2 = a + b + c - m1 - max(a, b, c)
if min(d, e) >= m1 and max(d, e) >= m2:
	print("YES")
else:
	print("NO")
