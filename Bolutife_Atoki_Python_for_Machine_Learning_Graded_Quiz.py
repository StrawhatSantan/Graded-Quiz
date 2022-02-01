#Atoki Bolutife's Graded Quiz codes
#Hamoye ID: 146eb340cb01f000
import pandas as pd
#Question 11
Dataset = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = 'latin‑1')
print(Dataset.groupby('Item').sum())

#Question 12
Dataset = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = 'latin‑1')
print(Dataset.describe(include='all'))

#Question 13
Dataset = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = 'latin‑1')
print(Dataset.isnull().sum())

#Question 14
Dataset = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = 'latin‑1')
Dataset.corr(method='pearson')

#Question 15
Dataset = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = 'latin‑1')
print(Dataset.groupby('Element').sum())

#Question 16
Dataset = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = 'latin‑1')
print(Dataset.groupby('Element').sum())

#Question 17
Dataset = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = 'latin‑1')
print(Dataset[['Y2018','Element']].groupby('Element').sum())

#Question 18
Dataset = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = 'latin‑1')
selection = Dataset[['Y2018','Element']].groupby('Element').sum()
print(selection.sort_values(by='Y2018'))

#Question 20
Dataset = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = 'latin‑1')
selection = Dataset[['Y2018','Area']].groupby('Area').count()
print(selection)