"""

클래스 메서드 @classmethod : 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용

"""


class Person(object):
	count = 0

	def __init__(self):
		Person.count += 1

	@classmethod
	def print_count(cls):
		print('{}명 생성 되었습니다.'.format(cls.count))  # cls로 클래스 속성에 접근

	@classmethod
	def create(cls):
		p = cls()
		return p


if __name__ == '__main__':
	moon = Person()
	kim = Person()
