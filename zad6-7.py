import numpy as np

def przekatne(n):
    macierz = np.arange(n*n)
    macierz = macierz.reshape((n,n))
    for i in range(1, n+1):
        x = np.diag([(i + 1) * 2], i)
        y = np.diag(i, [(i + 1) * 2])
return macierz

print(przekatne(3))

macierz = np.arange(3*3)
macierz = macierz.reshape((3,3))
for i in range(1, 4):
	x = np.diag([(i + 1) * 2], i)
	y = np.diag(i, [(i + 1) * 2])

print(x)