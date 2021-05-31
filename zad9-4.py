import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('iris.data', delimiter=',', header=None)
#print(df)
wykres = df.plot.scatter(x=1, y=2, c=3, colormap='viridis')
wykres.set_ylabel('petal length')
wykres.set_xlabel('sepal width')
plt.show()