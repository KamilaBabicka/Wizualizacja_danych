def funkcja(tekst):
    znaki = {x:tekst.count(x) for x in tekst}
    return znaki
print(funkcja("Testujemy czy dziala"))
    