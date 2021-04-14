def funkcja(tekst):
    x = input("Podaj nazwe pliku\n")
    tekst = tekst.lower()
    tekst2 = tekst.replace(".", "").replace(",","").split(" ")

    with open(x + ".txt", 'w') as plik:
        plik.write('\n'.join([i for i in tekst2 if tekst.count(i) == 1]))

test = "Ala, ma kota."
print(funkcja(test))



