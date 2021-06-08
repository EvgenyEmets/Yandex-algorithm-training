n = int(input())
s = set()
for i in range(n):
    inp = list(map(int, input().split()))
    s.add(inp[0])
print(len(list(s)))
