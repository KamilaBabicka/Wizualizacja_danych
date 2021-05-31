import pandas as pd
import numpy as np
import openpyxl 
plik = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(plik)