n, k, m = map(int, input().split())
ans = 0
while n >= k and k >= m:
	det = int(n/k)
	n %= k
	ans += int(k/m)*det
	n += det*(k%m)
print(ans)
