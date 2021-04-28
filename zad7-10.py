import numpy as np
a = np.arange(81).reshape(9, 9)
b = a.reshape(27, 3)
c = a.reshape(3, 27)
d = a.reshape(1, 81)
e = a.reshape(81, 1)

print(a)
print(b)
print(c)
print(d)
print(e)