def tostr(a):
    if a >= 0:
        return str(a)
    else:
        return "*"
    
n, m, k = map(int, input().split())
a = [0] * n
for i in range(n):
    a[i] = [0] * m
for i in range(k) :
    c = list(map(int, input().split()))
    a[c[0]-1][c[1]-1] = -1
for i in range(n):
    for j in range(m):
        if a[i][j] != -1:
            if i != 0:
                if j != 0:
                    if a[i-1][j-1] == -1:
                        a[i][j] += 1
                if j != m-1:
                    if a[i-1][j+1] == -1:
                        a[i][j] += 1
                if a[i-1][j] == -1:
                    a[i][j] += 1
            if i!= n-1:
                if j != 0:
                    if a[i+1][j-1] == -1:
                        a[i][j] += 1
                if j != m-1:
                    if a[i+1][j+1] == -1:
                        a[i][j] += 1
                if a[i+1][j] == -1:
                    a[i][j] += 1
            if j != 0:
                if a[i][j-1] == -1:
                    a[i][j] += 1
            if j != m-1:
                if a[i][j+1] == -1:
                    a[i][j] += 1
for i in a:
    print(" ".join(map(tostr, i)))
