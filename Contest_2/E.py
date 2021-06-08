n = int(input())
a = list(map(int, input().split()))
win = max(a)
prob = []
flg = False
for i in range(n-1):
	if flg and a[i] % 10 == 5 and a[i+1] < a[i]:
		if a[i] not in prob:
			prob.append(a[i])
	if a[i] == win:
		flg = True
if len(prob) != 0:
	vas = max(prob)
else:
	vas = win + 1
ans = 0
for i in a:
	if i > vas:
		ans += 1
if ans != 0:
	ans += 1
if vas == win:
	ans = 1
print(ans)
