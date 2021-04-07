class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print("Nazwa:", self.nazwa_produktu, "Ilość:", self.ilosc,"\t", "Jednoska:",self.jednostka_miary, "\t", "Cena:", self.cena_jed, "\n")
    
    def ile_produktu(self):
            print(self.ilosc, self.jednostka_miary)

    def ile_kosztuje(self):
        print(float(self.ilosc) * float(self.cena_jed))

produkt = NaZakupy("Jabłka", 7, "kg", 2)
produkt1 = NaZakupy("Mango", 15, "szt", 5)

produkt.wyswietl_produkt()
produkt.ile_produktu()
produkt.ile_kosztuje()

produkt1.wyswietl_produkt()
produkt1.ile_produktu()
produkt1.ile_kosztuje()