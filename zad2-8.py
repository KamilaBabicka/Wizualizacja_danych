import sys
lista = []
a = 0
while(a<5):
    b = sys.stdin.readline()
    lista.append(b)
    a+=1
sys.stdout.write(str(lista))