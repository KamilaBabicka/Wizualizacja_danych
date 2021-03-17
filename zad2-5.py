a = int(input("Podaj liczbe a\n"))
b = int(input("Podaj liczbe b\n"))
c = int(input("Podaj liczbe c\n"))
if (a > 0 and a <= 10) and (a > b or b > c):
    print("Warunki sa spelnione\n")
else:
    print("Warunki nie sa spelnione")