a = input()
b = input()
s1 = set()
s2 = set()
for i in range(len(a)-1):
    s1.add(a[i:i+2])
for i in range(len(b)-1):
    s2.add(b[i:i+2])
s = s1.intersection(s2)
count = 0
for i in range(len(a)-1):
    if a[i:i+2] in s:
        count += 1
print(count)
