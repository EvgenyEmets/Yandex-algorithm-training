a = set(map(int, input().split()))
b = int(input())
c = set()
while b > 0:
    c.add(b%10)
    b = int(b/10)
print(len(list(c.difference(a))))
