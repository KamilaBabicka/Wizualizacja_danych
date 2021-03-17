tekst = """Lorem Ipsum"""

#centrowanie
print('{:^20}'.format(tekst)) 
#wyrównanie do prawej
print('{:20}'.format(tekst)) 
#wyrównanie do lewej
print('{:>20}'.format(tekst)) 
#padding z prawej strony
print('{:_<20}'.format(tekst)) 
#truncating
print('{:.5}'.format(tekst)) 
