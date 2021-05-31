import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

grupowanie = df.groupby(['Plec']).agg({'Liczba': ['sum']}).unstack()
grupowanie.plot.bar(color=['y','b'])
plt.ylabel('Liczba urodzonych dzieci')
plt.xlabel('Płeć')
plt.legend()
plt.show()