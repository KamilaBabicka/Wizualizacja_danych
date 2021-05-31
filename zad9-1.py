import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

imiona_xlsx = pd.ExcelFile('imiona.xlsx')
imiona = pd.read_excel(imiona_xlsx)

df = imiona.groupby('Rok').agg({'Liczba': 'sum'})
df.plot()
plt.ylabel("Liczba urodzonych dzieci względem roku")
plt.show()

