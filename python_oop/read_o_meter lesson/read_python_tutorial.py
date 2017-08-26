
with open('story.txt', 'r') as story:
	all_words = story.readlines()
	print(len(all_words))

with open('story.txt', 'r') as story:
	for line in story:
		print(line)