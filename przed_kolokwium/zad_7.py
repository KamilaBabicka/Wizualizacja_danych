import random
def funkcja(ile, przedzial):
    los = []
    for x in range(int(ile)):
        z = random.randint(*przedzial)
        los.append(z)
    suma = 0
    for y in range(len(los)):
        suma += los[y]
    srednia = suma / len(los)
    return los, suma, srednia
print(funkcja(5,(1, 10)))