class Fighter:
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage = 10
		

# when one player attacks another player

	def attack(self, other_guy):
		other_guy.health = other_guy.health - self.damage
		print("{} attacks {}!!".format(self.name, other_guy.name))
		print("{} loses {} health points!!".format(other_guy.name, other_guy.damage))

# The string that is returned from a player's name

	def __str__(self):
		return "{} {}".format(self.name, self.health)


# players

denis = Fighter("Denis")
nicole = Fighter("Nicole")


print(denis)
print(nicole)

# denis attacks nicole

denis.attack(nicole)
print(nicole)



class Boxer(Fighter):
	def heal(self):
		self.health += 10
		


		
		



boxer_denis = Boxer("Denis")
print(boxer_denis)
print(boxer_denis.damage)
print(boxer_denis.health)

boxer_denis.heal()
print(boxer_denis)






