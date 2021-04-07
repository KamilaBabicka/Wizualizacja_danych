def cos(slowo):
    samogloski = ["a", "e", "i", "o", "u", "y"]
    abc = []
    for i in range(len(slowo)):
        for j in range(len(slowo)):
            if (slowo[i] == samogloski[j]):
                abc.append(slowo[i])
    yield abc

word = cos("jabłko")
print(next(word))


