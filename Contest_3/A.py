a = list(map(int, input().split()))
b = set()
count = 0
for i in a:
    if i not in b:
        b.add(i)
        count += 1
print(count)
