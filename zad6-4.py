import numpy as np

def potega(x, y):
    tab = np.logspace(1, y, num=y, base=x)
    return tab
print(potega(2,10))

