a = list(map(int, input().split()))
flg = True
lst = a[0]
for i in range(1, len(a)):
    if lst < a[i]:
        lst = a[i]
    else:
        flg = False
        break
if flg:
    print("YES")
else:
    print("NO")
