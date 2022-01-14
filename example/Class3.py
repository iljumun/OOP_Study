
"""

정적 메서드 @staticmethod : 클래스에서 바로 접근 가능

"""


class Calc(object):
	@staticmethod
	def add(a, b):
		print(a + b)

	@staticmethod
	def mul(a, b):
		print(a * b)


if __name__ == '__main__':
	Calc.add(1, 2)
	Calc.mul(2, 2)
