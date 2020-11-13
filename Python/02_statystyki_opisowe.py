import pandas as pd
from datetime import date

today = date.today()

# Exercise 1
df = pd.read_csv('arkusz.csv')
df['Data_urodzenia'] = pd.to_datetime(df['Data_urodzenia'])
df['Staż_pracy'] = df['Staż_pracy'].astype(int)
df['Wiek'] = df.apply(lambda row: today.year - row[1].year - ((today.month, today.day) < (row[1].month, row[1].day)),
                      axis=1)
df['Rok_rozpoczęcia_pracy'] = df.apply(lambda row: today.year - row['Staż_pracy'], axis=1)


# print(df)

# Exercise 2
def kwart(row):
    if 1 <= row['Data Faktury'].month <= 3:
        return 1
    elif 4 <= row['Data Faktury'].month <= 6:
        return 2
    elif 7 <= row['Data Faktury'].month <= 9:
        return 3
    else:
        return 4


dfs = pd.read_excel('faktury.xls', sheet_name='faktury')
dfs['miesiac'] = dfs.apply(lambda row: row['Data Faktury'].month, axis=1)
dfs['wartosc'] = dfs.apply(lambda row: row['ilośc towaru'] * row['cena towaru'], axis=1)
dfs['kwartal'] = dfs.apply(lambda row: kwart(row), axis=1)
# print(dfs.head())

# Exercise 3
dfs1 = dfs.loc[dfs['Data Faktury'] > '2005-12-31']
dfs2 = dfs1[['nr faktury', 'Data Faktury', 'NIP', 'wartosc', 'miesiac', 'kwartal']]
# dfs2.to_stata('faktury2005.sta')

# Exercise 4

# ndf = dfs.loc[dfs['Data Faktury'].dt.year == 2007]['wartosc']
# print("Min: ",np.min(ndf))
# print("Max: ",np.max(ndf))
# print("Median: ",np.median(ndf))
# print("Moda: ",max(set(ndf.values.tolist()), key=ndf.values.tolist().count))
# print("Kurtosis: ",ndf.kurtosis())
# print("Skewnes: ",ndf.skew())

# Exercise 5
# ndf1 = dfs.loc[dfs['płatność'] == 'gotowka']['wartosc']
# print("Min: ",np.min(ndf1))
# print("Max: ",np.max(ndf1))
# print("Median: ",np.median(ndf1))
# print("Moda: ",max(set(ndf1.values.tolist()), key=ndf1.values.tolist().count))
# print("Kurtosis: ",ndf1.kurtosis())
# print("Skewnes: ",ndf1.skew())

# Exercise 6
dfp = pd.read_excel('Pracownicy.xls', header= None)
print(dfp.head())
