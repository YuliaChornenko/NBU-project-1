import pandas as pd

df = pd.read_csv('../data/nbu.csv')

df.drop(df[(df.category == '1') | (df.category == '0')].index, inplace=True)

positive = df[(df.category == 'Positive')].sample(frac=1).reset_index(drop=True)[:50]
negative = df[(df.category == 'Negative')].sample(frac=1).reset_index(drop=True)[:50]
hotline = df[(df.category == 'Hotline')].sample(frac=1).reset_index(drop=True)[:50]
hooligan = df[(df.category == 'Hooligan')].sample(frac=1).reset_index(drop=True)[:50]
siteandcoins = pd.read_csv('../data/coins.csv')[:50]

DF = pd.concat([positive, negative, hotline, hooligan, siteandcoins])
DF.to_csv('data/category.csv', index=False)