import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

grupowanie = df[df['Rok'] > 2012].groupby(['Plec']).agg({'Liczba': ['sum']})
wykres = grupowanie.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title('Ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach')
plt.show()
