def generator():
    nazwy = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
    for x in nazwy:
        yield x

test = generator()

for y in range (1,13,1):
    print(next(test))
