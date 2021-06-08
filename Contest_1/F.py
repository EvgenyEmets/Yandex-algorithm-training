a, b, c, d = map(int, input().split())
c1 = [a, b]
c2 = [c, d]
mins = (a+c) * (b+d)
best = [a+c, b+d]
for i in range(2):
    for j in range(2):
        if (c1[i]+c2[j])*max(c1[(i+1)%2], c2[(j+1)%2]) < mins:
            mins = (c1[i]+c2[j])*max(c1[(i+1)%2], c2[(j+1)%2])
            best = [c1[i]+c2[j], max(c1[(i+1)%2], c2[(j+1)%2])]
print(*best)
