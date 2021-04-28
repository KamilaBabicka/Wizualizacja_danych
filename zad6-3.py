import numpy as np

def funkcja(n):
    liczby = [x for x in range(1,n*n+1)]
    a = np.array([liczby[y*n : y*n+n] for y in range(int(len(liczby)/n))])
    return a

print(funkcja(10))


