a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a*d - b*c != 0:
	y = (f*a-c*e)/(d*a-c*b)
	x = 0
	if a != 0:
		x = (e-b*y)/a
	else:
		x = (f-d*y)/c
	print(2, x, y)
else:
	if a != 0 or b != 0 or c != 0 or d != 0:
		if a*f-c*e != 0 or b*f-d*e != 0:
			print(0)
		elif a == 0 and c == 0:
			if b != 0:
				print(4, e/b)
			else:
				print(4, f/d)
		elif b == 0 and d == 0:
			if a != 0:
				print(3, e/a)
			else:
				print(3, f/c)
		else:
			if b != 0:
				print(1, -a/b, e/b)
			else:
				print(1, -c/d, f/d)
	else:
		if e != 0 or f != 0:
			print(0)
		else:
			print(5)
