# building --> to build
# build --> not a gerund

# cmd + k cmd + b. --> hide sidebar

# building
# remove the ing
# add "to" with a space after in front of the word.

# 1. building
# 2. build
# 3. to build

# How do we say the last 3 letters in python?
# last 3 letters --> word[-3:]
# if the last 3 letters are not equal to 'ing' return "not a gerund"
# if 'ing' then return the word up the the final 3 letters. --> word[:-3]
# add 'to ' to the start of word[:-3]


def gerund_infinit(word):
	if word[-3:] != 'ing':
		return 'not a gerund'
	else:
		return 'to ' + word[:-3]


def tests():
	assert gerund_infinit('toying') == "to toy"
	assert gerund_infinit('banana') == 'not a gerund'


tests()