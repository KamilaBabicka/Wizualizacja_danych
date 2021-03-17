import sys
h = int(sys.stdin.readline())
if h>10: 
    print("Wysokość musi być mniejsza niż 10")
for x in range(0, h+1):
    wieza = "A"*x
    print(wieza)