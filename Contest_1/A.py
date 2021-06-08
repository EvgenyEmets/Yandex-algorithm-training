a, b = map(int, input().split())
mode = input()
if mode == "fan":
	print(a)
elif mode == "auto":
	print(b)
elif mode == "heat":
	print(max(a, b))
elif mode == "freeze":
	print(min(a, b))
