def monotonicznosc(a):
    if (a>0):
        print("Funkcja jest rosnaca")
    elif (a<0):
        print("Funkcja jest malejaca")
    else:
        print("Funkcja jest stala")

print(monotonicznosc(-6))
print(monotonicznosc(6))
print(monotonicznosc(0))