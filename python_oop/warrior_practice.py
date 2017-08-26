# A warriors class that takes input for name, health and weapon
# The attack method takes 14 points off the opponents health
# Each opponent starts with a different level of health
# The print statements record the result with some fight commentary

class Warriors:
	def __init__(self, name, health, weapon):
		self.name = name
		self.health = health
		self.weapon = weapon
		self.damage = 14

	def attack(self, opponent):
		opponent.health = opponent.health - self.damage


denis = Warriors("Denis", 110, "axe and sword")
jessica = Warriors("Jessica", 90, "crossbow")
rob = Warriors("Rob", 59, "flamethrower")
deepak = Warriors("Deepak", 96, "knuckledusters")

print("It's fight night!!")

print("Our opponents tongiht are:  Denis, Jessica, Rob and Deepak")
print("Here are our opponents weapons: ")

print("Denis' weapon of choice: ")
print(denis.weapon)
print("Jessica's weapon of choice: ")
print(jessica.weapon)
print("Rob's weapon of choice: ")
print(rob.weapon)
print("Deepak's weapon of choice: ")
print(deepak.weapon)


print("Let's fight!")




denis.attack(jessica)
jessica.attack(rob)
rob.attack(jessica)
rob.attack(deepak)
rob.attack(jessica)
denis.attack(rob)
denis.attack(deepak)
deepak.attack(denis)
rob.attack(denis)
jessica.attack(denis)

print("Jessica's health: ")
print(jessica.health)
print("Rob's health: ")
print(rob.health)
print("Deepak's health: ")
print(deepak.health)
print("Denis' health: ")
print(denis.health)

print("Wow, we have a draw between Denis and Deepak!")
print("Time for sudden death")

denis.attack(deepak)
deepak.attack(denis)
denis.attack(deepak)
denis.attack(deepak)
deepak.attack(denis)
denis.attack(deepak)
denis.attack(deepak)

print("Deepak's health")
print(deepak.health)
print("Denis' health: ")
print(denis.health)


print("The winner is the Notorious one.")
print("Congrats Denis!")
print("Denis: 'Thank You!! I am humble in victory or defeat :) ")




