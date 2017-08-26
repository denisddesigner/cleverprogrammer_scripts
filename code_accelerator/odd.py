# write a function biggest_guy that takes three numbers as input and returns the biggest one

def biggest_guy(num1, num2, num3):
	return max(num1, max(num2, num3))

print(biggest_guy(9, 30, 59))

