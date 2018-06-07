class Student():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@property
	def get_age_formatted(self):
		return "%s years old" % self.age