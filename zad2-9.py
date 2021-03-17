import sys

suma = 0
liczba = int(sys.stdin.readline())
while(liczba!=0):
    suma = suma + int(liczba % 10)
    liczba = int(liczba / 10)
sys.stdout.write(str(suma))