plik = open("liczby1.txt","w+")
for x in range(1,100,1):
   if(x%4 == 0):
    plik.write(str(x))
    plik.write("\n")
