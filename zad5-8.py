class Samogloski:
    def __init__(self, slowo):
        if isinstance(slowo, str):
            self.slowo = slowo
        else:
            return "To nie jest słowo!"

    def __iter__(self):
        return self

    def __next__(self):
        wynik = []
        samogloski = ["a", "ą", "e", "ę", "i", "o", "ó", "u", "y"]
        for i in range(len(self.slowo)):
            for j in range(len(self.slowo)):
                if(self.slowo[i] == samogloski[j]):
                    wynik.append(self.slowo[i]) 
        return wynik

word = Samogloski("Jabłko")
print(word.__next__())