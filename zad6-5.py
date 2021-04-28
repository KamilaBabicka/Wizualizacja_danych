import numpy as np

def funkcja(n):
    wektor = [x for x in range(1, n+1)][::-1]
    macierz = np.diag([y for y in wektor])
    return macierz
print(funkcja(5))