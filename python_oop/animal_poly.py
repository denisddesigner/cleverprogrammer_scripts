class Animal:
	def __init__(self, name):
		self.name = name

	def talk(self):
		pass

pet_denis = Animal("Denman")

print(pet_denis.name)
print(pet_denis.talk())

class Dog(Animal):
	def talk(self):
		return "WOOF"

class Cat(Animal):
	def talk(self):
		return "MEOW"

class Sheep(Animal):
	def talk(self):
		return "Bahh"

	def complain(self):
		return "Why are you annoying me?!!!?!!!"

pet = Dog("Dot")
print(pet.name)
print(pet.talk())

kitten = Cat("Tabby")
print(kitten.name)
print(kitten.talk())

sheep = Sheep("Sean")
print(sheep.name)
print(sheep.talk())
print(sheep.complain())


