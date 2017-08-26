def word_counter(text):

	return len(sentence.split(' '))

#print(word_counter('this is a sentence'))











story = 'Once upon a time there was a lot of words to write here and i want to see if this works or not hopeufllugfds i to waoks an d not this is starting to look like gibbersj..'

def word_counter(text):

	bucket = (text.split(' '))

	return len(bucket)



print(word_counter(story))


# word_count/200 --> average reading time (minutes)

def average_read_time(word_count):

	return word_count/200

print(average_read_time(word_counter(story)))


def final_app(text):
	return average_read_time(word_counter(story))

print(final_app(story))







