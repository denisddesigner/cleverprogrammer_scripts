"""
Problem Link: https://projecteuler.net/problem=3
Problem: Given a number,return it's largest prime factor
Author: Denis
Date Modified: April 2017
"""

# A prime number is only divisible by itself and the number 1. A prime number is > 1
# Given a number return it's largest prime factor

# Return the prime numbers that divide into the number 15
# The following prime numbers divide into 15: 3 and 5
# The final answer is 5 because it is the largest prime factor

# Let's say we are given 15
# What are the prime factors of 15?
# [3, 5]
# index list on line 16 by -1 and you'll get the largest prime factor

# n = 37

# largest_prime_factor(n)

# largest_prime_factor(10) --> 5
# largest_prime_factor(15) --> 5

def prime_number_test(number):

	list = []

	if number > 1:
		for i in range(2, number):
			if number % i == 0:
				list.append(i)
	
				
	return max(list) 





print(prime_number_test(600))


















