import pandas as pd

df = pd.read_csv('data/nbu.csv')

df.drop(df[(df.category == '1') | (df.category == '0')].index, inplace=True)

n = 66

positive = df[(df.category == 'Positive')].sample(frac=1).reset_index(drop=True)[:n]
negative = df[(df.category == 'Negative')].sample(frac=1).reset_index(drop=True)[:n]
hotline = df[(df.category == 'Hotline')].sample(frac=1).reset_index(drop=True)[:n]
hooligan = df[(df.category == 'Hooligan')].sample(frac=1).reset_index(drop=True)[:n]
siteandcoins = pd.read_csv('data/coins.csv')[:n]

DF = pd.concat([positive, negative, hotline, hooligan, siteandcoins])
DF.to_csv('data/category.csv', index=False)