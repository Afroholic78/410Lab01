class Student:
	courseMarks={}
	name=""
	average = 0
	def __init__(self,name,family):
		self.name = name + " " +family

	def addCourseMark(self, course, mark):
		self.courseMarks[course] = mark

	def average(self):
		average = 0;
		for x in self.courseMarks:
			average += self.courseMarks[x]
		if len(self.courseMarks):
			self.average = average/len(self.courseMarks)

S = Student("Ash", "Ketchum")
S.addCourseMark("410", 4)
S.addCourseMark("401", 0)
S.average()
print(S.name)
print(S.courseMarks)
print(S.average)

