class Person(object):
	'''사람 클래스 입니다.'''  # __doc__ 독스트링
	bag = list()  # 클래스 속성은 모든 인스턴스에 공용
	
	def __init__(self):
		self.bag = list()  # 인스턴스 마다 bag 생성 (클래스 속성보다 우선순위 높음)

	def put_bag(self, stuff):
		'''가방메서드 입니다.'''
		self.bag.append(stuff)


if __name__ == '__main__':
	moon = Person()
	kim = Person()

	moon.put_bag('책')
	kim.put_bag('담배')

	print(moon.bag)
	print(kim.bag)

	print(moon.__doc__)
	print(moon.put_bag.__doc__)
