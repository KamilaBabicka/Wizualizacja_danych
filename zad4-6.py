class Slowa:
    def __init__(self, pierwsze_slowo, drugie_slowo):
        self.pierwsze_slowo = pierwsze_slowo
        self.drugie_slowo = drugie_slowo

    def czy_palindrom(self):
        if self.pierwsze_slowo == self.pierwsze_slowo[::-1]:
            print(f"{self.pierwsze_slowo} to palindrom.")
        else:
            print(f"{self.pierwsze_slowo} to nie palindrom.")
        if self.drugie_slowo == self.drugie_slowo[::-1]: 
            print(f"{self.drugie_slowo} to palindrom.")
        else:
            print(f"{self.drugie_slowo} to nie palindrom.")

    def czy_metagramy(self):
        rozne = 0
        if len(self.pierwsze_slowo) == len(self.drugie_slowo):
            for x in range(len(self.pierwsze_slowo)):
                if self.pierwsze_slowo[x] != self.drugie_slowo[x]:
                    rozne += 1
        if rozne == 1:
            print("Podane słowa to metagramy.")
        else: 
            print("Podane słowa nie są metagramami.")

    def czy_anagramy(self):
        if sorted(self.pierwsze_slowo) == sorted(self.drugie_slowo):
            print(f"{self.pierwsze_slowo} i {self.drugie_slowo} to anagramy.")
        else:
            print(f"{self.pierwsze_slowo} i {self.drugie_slowo} nie są anagramami.")

    def wyswietl_wyrazy(self):
        print(f'{self.pierwsze_slowo}, {self.drugie_slowo}')

palindrom = Slowa("kajak", "kosz")
anagramy = Slowa("tama", "mata")
metagramy = Slowa("mata", "tata")
print(palindrom.wyswietl_wyrazy())
print(palindrom.czy_palindrom())

print(metagramy.wyswietl_wyrazy())
print(metagramy.czy_metagramy())

print(anagramy.wyswietl_wyrazy())
print(anagramy.czy_anagramy())
