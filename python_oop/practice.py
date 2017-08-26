def fibonacci(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
	return(a)
# fibonacci sequence = 0, 1, 1, 2, 3, 5, 8, 13, 21
# 23, 24, 47, 71, 118, 189, 307

print(fibonacci(4))












