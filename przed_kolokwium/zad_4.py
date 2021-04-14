def liczby(ciag):
    najwieksze = sorted(ciag, reverse=True)
    return najwieksze[0:3]

print(liczby([1,2,4124,523,124,5,2312,45,212,643,51324,32,6234,14,24,1235,234,12]))
