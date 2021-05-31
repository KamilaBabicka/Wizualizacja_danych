import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("zamowienia.csv", delimiter=';')

grupowanie = df.groupby(["Sprzedawca"])["idZamowienia"].count()
wykres = grupowanie.plot.bar(color=['r','b','g','c','m','y','k', 'lime', 'pink'])
wykres.legend()
plt.show()

