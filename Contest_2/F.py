def issim(a):
    b = a[-1::-1]
    return a == b

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    inv = []
    inv = a[0:i]
    inv = inv[-1::-1]
    t = []
    t.extend(a)
    t.extend(inv)
    if issim(t):
        print(i)
        if len(inv) != 0:
            print(" ".join(map(str, inv)))
        break
