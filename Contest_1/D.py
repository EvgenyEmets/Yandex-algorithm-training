a = int(input())
b = int(input())
c = int(input())
if c < 0:
	print("NO SOLUTION")
elif a == 0:
	if b >= 0 and b == c**2:
		print("MANY SOLUTIONS")
	else:
		print("NO SOLUTION")
else:
	x = int((c**2 - b) / a)
	if (a * x + b)**0.5 == c:
		print(x)
	else:
		print("NO SOLUTION")
