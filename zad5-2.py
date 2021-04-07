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

kw = Kwadrat(5)
kw1 = Kwadrat(10)

kw3 = kw.__add__(kw1)
print(kw3)

