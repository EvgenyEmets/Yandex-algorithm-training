def pars(s):
    b = ""
    for i in s:
        if i != "-" and i != "(" and i != ")":
            b += i
    code = ""
    num = ""
    if len(b) > 7:
        if b[0] == "+":
            b = b[2:]
        else:
            b = b[1:]
        code = b[:3]
        num = b[3:]
    else:
        code = "495"
        num = b
    return code + num

def comp(a, b):
    if a == b:
        print("YES")
    else:
        print("NO")

a = pars(input())
b = pars(input())
c = pars(input())
d = pars(input())
comp(a, b)
comp(a, c)
comp(a, d)
