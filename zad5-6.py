class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

wyraz1 = Wspak("Jabłko")
for x in range(wyraz1.index):
    print(wyraz1.__next__())
print("----------")

wyraz2 = Wspak("Koloseum")
for y in range(wyraz2.index):
    print(wyraz2.__next__())
print("----------")
