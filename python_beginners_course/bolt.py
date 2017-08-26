# given the name return the place - Usain 1st, Denis 2nd, Qazi 3rd

def choice_to_number(choice):
	if choice == 'Usain':
		return 1
	elif choice == 'Denis':
		return 2
	elif choice == 'Qazi':
		return 3
	else:
		return 'Not placed'

print(choice_to_number("Anna"))




# given the number return the name - Usain 1st, Denis 2nd, Qazi 3rd

def number_to_choice(number):
	if number == 1:
		return 'Usain'
	elif number == 2:
		return 'Denis'
	elif number == 3:
		return 'Qazi'
	else:
		return 'does not compute'


print(number_to_choice(4))



# bonus

def dict_to_number(choice):
	return {'Usain': 1, "Denis": 2, "Qazi": 3}[choice]

print(dict_to_number('Usain'))


def dict_to_place(place):
	return{1: 'Usain' , 2: 'Denis', 3: 'Qazi'}[place]

print(dict_to_place(1))





























