import numpy as np
a = np.arange(12)
b = a.reshape(3, 4)
c = a.reshape(4, 3)
d = a.reshape(2, 6)
print(a)
print(a.ravel())
print(b)
print(b.ravel())
print(c)
print(c.ravel())
print(d)
print(d.ravel())