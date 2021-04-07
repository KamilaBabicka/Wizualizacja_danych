class Ciag:
	def __init__(self):
		self.elementy = []
		self.a1 = 0
		self.r = 1
		self.ilosc = 0

	def wyswietl_dane(self):
		print(self.elementy)

	def pobierz_elementy(self, *elem):
		self.elementy.append(elem)

	def pobierz_parametry(self):
		self.a1 = int(input("Podaj a1:"))
		self.ilosc = int(input("Podaj ilosc elementow:"))
		self.r = int(input("Podaj r:"))

	def policz_sume(self):
		return sum(self.ciagi)

	def policz_elementy(self):
		return len(self.ciagi)

test1 = Ciag()
test1.pobierz_elementy()
test1.pobierz_parametry()
print(test1.policz_sume())
print(test1.policz_elementy())
test1.wyswietl_dane()
