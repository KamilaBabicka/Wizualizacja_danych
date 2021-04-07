class Material:
    def __init__ (self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(f"Materiał: {self.rodzaj}\nWymiary: {self.dlugosc}x{self.szerokosc}")
    
class Ubrania(Material):
    def __init__ (self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo
    
    def wyswietl_dane(self):
        print(f"Rozmiar: {self.rozmiar} Kolor: {self.kolor}, Dla kogo: {self.dla_kogo}")
    
class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra):
       self.rodzaj_swetra = rodzaj_swetra
    
    def wyswietl_dane(self):
        print(f"Rodzaj: {self.rodzaj_swetra}")

material1 = Material("welur", 60, 40)
material2 = Material("bawełna", 70, 80)
ubrania1 = Ubrania(38, "czarny", "damski")
ubrania2 = Ubrania(40, "biały", "unisex")
sweter1 = Sweter("z golfem")
sweter2 = Sweter("rozpinany")

material1.wyswietl_nazwe()
sweter2.wyswietl_dane()
ubrania1.wyswietl_dane()

