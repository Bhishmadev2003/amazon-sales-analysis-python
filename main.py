import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Amazon Sale Report.csv', encoding='unicode_escape')
# print(df)
# print(f'shape: {df.shape}')
# print(df.head())
# print(df.tail())
# print(df.info()) #got two blank coloumns
df.drop(['New', 'PendingS'], axis=1, inplace=True) #for deleting all blank coloumns
# print(df.info()) #clean
# print(pd.isnull(df).sum())
# print(f'shape: {df.shape}')
df.dropna(inplace=True) #for deleting all nul values

# print(f'shape: {df.shape}')
# print(pd.isnull(df).sum())
# print(df.columns)
# print(df.info())
df['ship-postal-code']=df['ship-postal-code'].astype('int')
# print(df.info())

df['Date']=pd.to_datetime(df['Date'])
df.rename(columns={'Qty': 'Quantity'}, inplace=True)
print(df.describe())
print(df.info())
print(df)

#now data fully clean!