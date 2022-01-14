"""

*args : 인자로 list를 받음
**kwarge : 인자로 dict를 받음

"""


class Person(object):
	def __init__(self, **kwargs):
		self.hello = "안녕하세요?"
		self.name = kwargs['name']
		self.age = kwargs['age']
		self.address = kwargs['address']
		self.__wallet = kwargs['wallet']  # 비공개 속성

	"""
	def__init__(self, *args):
		self.hello = args[0]
		self.name = args[1]
		self.address = args[2]
	"""

	def __greeting(self):
		print("{} 저는 {}입니다.".format(self.hello, self.name))

	def pay(self, amount):
		self.__wallet -= amount

		if amount > self.__wallet:
			print('돈이 부족하네요?')
		else:
			print('영수증 확인해 보세요.')


if __name__ == '__main__':
	# jam = Person(*['조선제일문화백', '29', '오창읍'])
	jam = Person(name='조선제일문화백', age='29', address='오창읍', wallet=100000)
	moon = Person(**{'name': '조선제일문선생', 'age': '29', 'address': '오창읍', 'wallet': 100000})

	jam.pay(150000)
