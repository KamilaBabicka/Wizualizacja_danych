import numpy as np

x = np.arange(9).reshape(3,3)
print(x)

minx = x.min(axis=0)
minx1 = x.min(axis=1)
print(minx)
print(minx1)

y = np.arange(16).reshape(4,4)
print(y)

miny = y.min(axis=0)
miny1 = y.min(axis=1)
print(miny)
print(miny1)
