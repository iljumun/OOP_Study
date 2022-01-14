"""

상속, super()

"""


class Person(object):
	def __init__(self):
		self.hello = "안녕하세용?"

	def greeting(self):
		print(self.hello)


class Student(Person):
	def __init__(self):
		super().__init__()
		print("저는 학생입니다.")

	def study(self):
		print("공부하기.")


class PersonList(object):
	def __init__(self):
		self.person_list = list()

	def append_person(self, person):
		self.person_list.append(person)

	def print_person(self):
		print(self.person_list)


if __name__ == '__main__':
	moon = Person()
	moon2 = Student()

	moon.greeting()
	moon2.greeting()
	moon2.study()
	print(moon2.hello)  # super()로 부모 클래스 초기화 해줘야함.

	pl = PersonList()
	pl.append_person(moon2)
	pl.append_person(moon)
	pl.print_person()
