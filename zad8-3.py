import pandas as pd
import numpy as np
import openpyxl

df = pd.read_csv('zamowienia_ok.csv', delimiter=';')

# print(df['Sprzedawca'].unique())
# print(set(df['Sprzedawca'].values))
# print(set(df['Sprzedawca']))


# print(df.sort_values(by='Utarg', ascending=False)[0:5])
# print(df.sort_values(by='Utarg', ascending=False)['Utarg'][0:5])
# print(df.sort_values(by='Utarg', ascending=False)['Utarg'][0:5].values)

# print(df.groupby(['Sprzedawca']).size())
# print(df.groupby(['Sprzedawca']).count())
#print(df.groupby(['Sprzedawca']).size().sum())

# print(df.groupby(['Kraj']).agg({'Utarg':['sum']}))

# print(df[((df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31') & (df['Kraj'] == 'Polska'))].agg({'Utarg':['sum']}))

# print(df['Data zamowienia'].str[:4])
# print(df.groupby(df['Data zamowienia'].str[:4]).agg({'Utarg':['mean']}))
# print(df[((df['Data zamowienia'].str[:4] == '2004'))].agg({'Utarg': ['mean']}))
# print(df[((df['Data zamowienia'].str[:4] == '2004'))]['Utarg'].mean())


r2004 = df[((df['Data zamowienia'].str[:4] == '2004'))]
r2005 = df[((df[ 'Data zamowienia'].str[ :4 ] == '2005')) ]
    
r2004.to_csv("zamowienia_2004.csv", index=False)
r2005.to_csv("zamowienia_2005.csv", sep=';', index=False)

