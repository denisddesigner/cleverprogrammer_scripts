# change string to list with .split()
# create an empty dictionary and append words to dictionary with a value
# if word not in dictionary assign the value 1
# if already in dictionary increment value += 1
# test with assertions
# word frequency counter
# needs to be completed before next session!
# Good luck :)

sentence = 'hey what is up how is it going Denis. I was talking and then I was like what!'


def word_counter(words):

	special = './?:;!'

	for char in special:
		words = words.replace(char,'')
		
	words_list = words.split()

	dict_counter = dict()

	for word in words_list:
		if word not in dict_counter:
			dict_counter[word] = 1
		else:
			dict_counter[word] += 1
	return dict_counter



print(word_counter(sentence))



def test_word_counter():

	print('------RUNNING TESTS------')

	assert word_counter('hey how are you'), {'hey': 1}
	
	

	

	print('---Success at Last-----')

test_word_counter()




	