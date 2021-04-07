class Kwadrat: 
    def __init__(self, x):
        self.x = x

    def __radd__(self, a):
        if a == 0:
            return self
        else:
            return self.__add__(a)

    def __add__(self, a):
        return self.x + a

    def __add__(self, a):
        return self.x + a

    def __ge__(self, a):
        return self.x >= a

    def __gt__(self, a):
        return self.x > a

    def __le__(self, a):
        return self.x <= a

    def __lt__(self, a):
        return self.x < a

kw = Kwadrat(5)
kw1 = Kwadrat(10)
kw3 = kw.__add__(kw1)
print(kw3)

if kw.__ge__(kw1):
    print("Pierwszy kwadrat jest większy lub równy.")

if kw.__gt__(kw1):
    print("Pierwszy kwadrat jest większy.")

if kw.__le__(kw1):
    print("Pierwszy kwadrat jest mniejszy lub równy.")

if kw.__lt__(kw1):
    print("Pierwszy kwadrat jest mniejszy.")