n = int(input())
s = set()
for i in range(n):
    s.add(input())
count = 0
for i in s:
    j = list(map(int, i.split()))
    if j[0] + j[1] == n - 1 and j[0] >= 0 and j[1] >= 0:
        count += 1
print(count)
