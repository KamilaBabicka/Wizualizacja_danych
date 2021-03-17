import sys

print("Podaj 2 liczby\n")
liczba1 = int(sys.stdin.readline())
liczba2 = int(sys.stdin.readline())
wynik = liczba1*liczba2

sys.stdout.write(str(wynik))