tekst = input("Podaj tekst\n")
duze = 0
male = 0
for x in range (len(tekst)):
    if tekst[x].islower():
        male += 1
    elif tekst[x].isupper():
        duze += 1
print("Ilosc malych liter:", male)
print("Ilosc duzych liter:", duze)
