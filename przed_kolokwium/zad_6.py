def liczby():
    with open("liczby.txt", "r+") as plik:
        pom = [int(x) for x in plik.read().split()]
        plik.seek(0)
        plik.write("\n".join([str(x) for x in sorted(pom)]))

liczby()

