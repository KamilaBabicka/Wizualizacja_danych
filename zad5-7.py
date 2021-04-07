class Parzyste:
	def __init__(self, wartosc):
		self.wartosc = wartosc
		self.index = 0

	def __iter__(self):
		return self

	def __next__(self):
		wartosc = self.wartosc[self.index]
		self.index += 2
		return wartosc

obiekt = Parzyste("obiekt")
print(next(obiekt))
print(next(obiekt))
print(next(obiekt))