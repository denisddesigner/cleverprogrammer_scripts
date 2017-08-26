class Student:

	def __init__(self, name, grade, age, occupation):
		self.name = name
		self.grade = grade
		self.age = age
		self.occupation = occupation

zoe = Student("Zoe", 90, 18, "student")
dan = Student("Declan", 57, 26, "dentist")

print(zoe.name)
print(dan.name)

print(zoe.grade)
print(dan.grade)

print(zoe.age)
print(dan.age)

print(zoe.occupation)
print(dan.occupation)