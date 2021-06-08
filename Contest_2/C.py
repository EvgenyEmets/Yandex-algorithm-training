n = int(input())
a = list(map(int, input().split()))
x = int(input())
d = abs(x - a[0])
ans = a[0]
for i in range(1, n):
	d1 = abs(x - a[i])
	if d1 < d:
		d = d1
		ans = a[i]
print(ans)
