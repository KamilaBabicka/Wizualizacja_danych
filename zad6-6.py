import numpy as np
w1 = "szum"
w2 = "mata"
w3 = "mózg"
litery = "abcdefghijklmnop"
j = list(litery)

mat1 = np.array([j[y*4 : y * 4 + 4] for y in range(4)])
mat1 = np.diag(list(w1)[::-1])
mat1[0:4,0]=list(w3)
mat1[0,0:4]=list(w2)
print(mat1)
