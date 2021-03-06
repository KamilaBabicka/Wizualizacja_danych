class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik:
    def __init__(self, pensja):
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Osoba, Pracownik):
    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        Pracownik.__init__(self, pensja)

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


adrian = Menadzer("Adrian", "Mikulski", 12000)
piotr = Osoba("Piotr", "Adamski")

print(adrian.przedstaw_sie())
print(piotr.przedstaw_sie())

print(isinstance(adrian, Menadzer))
print(isinstance(adrian, Osoba))
print(isinstance(adrian, Pracownik))

print(isinstance(piotr, Menadzer))
print(isinstance(piotr, Osoba))
print(isinstance(piotr, Pracownik))

print(issubclass(Menadzer, Osoba))
print(issubclass(Menadzer, Pracownik))
print(issubclass(Pracownik, Osoba))
print(issubclass(Pracownik, Menadzer))
print(issubclass(Osoba, Menadzer))
print(issubclass(Osoba, Pracownik))