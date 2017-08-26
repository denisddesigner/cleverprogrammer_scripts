class BestCourse:
	website = "http://cleverprogrammer.com"

	def __init__(self, name):
		self.name = name

python_course = BestCourse("Learn Python")
learn_command_line_course = BestCourse("Learn Command Line")

print(python_course.name)
print(BestCourse.website)

print(learn_command_line_course.name) # object_name.method
print(BestCourse.website) # class_name.method
