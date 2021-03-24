import math

def okrag(x, y, a=0, b=0):
    return math.sqrt((x-a)**2 + (y-b)**2)

print(okrag(3, 4))
print(okrag(-1,-2, -4, -6))