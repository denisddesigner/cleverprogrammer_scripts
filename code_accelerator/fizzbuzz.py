# fizzbuzz
# spectacle window management tool or window magnet 

# print from 1 to 100, if the number is divisible by 3 print 'fizz'
# if the number is divisible by 5 print 'buzz'
# if divisible by 3 and 5 fizzbuzz
# else print number

# 1 --> 1
# 2 --> 2
# 3 --> fizz
# 4 --> 4
# 5 --> buzz
# 6 --> fizz
# 7 --> 7
# 8 --> 8
# 9 --> fizz
# 10 --> buzz
# 11 --> 11
# 12 --> fizz
# 13 --> 13
# 14 --> 14
# 15 --> fizzbuzz


def fizzbuzz(num1, num2):
	for number in range(num1, num2):
		if number % 3 == 0 and number % 5 == 0:
			print('fizzbuzz')
		elif number % 3 == 0:
			print('fizz')
		elif number % 5 == 0:
			print('buzz')
		else:
			print(number)

fizzbuzz(10, 100)





