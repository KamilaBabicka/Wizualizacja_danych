def zakupy(** lista):
    ilosc = 0.0
    for x in lista:
        ilosc+= lista[x]
    return ilosc

print(zakupy(mleko=3, maslo=5))
   