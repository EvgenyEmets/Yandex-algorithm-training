n, m = map(int, input().split())
a = set()
b = set()
for i in range(n):
    a.add(int(input()))
for i in range(m):
    b.add(int(input()))
c = a.intersection(b)
print(len(list(c)))
print(*sorted(c))
d1 = a.difference(c)
print(len(list(d1)))
print(*sorted(d1))
d2 = b.difference(c)
print(len(list(d2)))
print(*sorted(d2))