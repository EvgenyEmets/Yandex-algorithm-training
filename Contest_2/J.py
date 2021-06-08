n = int(input())
a = [30, 4000]
g = float(input())
for i in range(n-1):
    c = input().split()
    c[0] = float(c[0])
    edge = (g + c[0])/2
    if c[1] == "closer":
        if c[0] < g: 
            if a[1] > edge:
                a[1] = edge
        else:
            if a[0] < edge:
                a[0] = edge
    else:
        if c[0] > g: 
            if a[1] > edge:
                a[1] = edge
        else:
            if a[0] < edge:
                a[0] = edge
    g = c[0]
print(*a)
