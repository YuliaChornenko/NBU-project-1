import pandas as pd
import re

df = pd.read_csv('data/data.csv')

df.drop(df[(df.category == '1') | (df.category == '0')].index, inplace=True)

df = df[~df['text'].str.contains('?')]
print(df)

# i=0
# for line in df.text:
#     match = re.search('[?]', line)
#     if (df.category[i] == 'Positive' or df.category[i] == 'Negative') and match != None :
#         print(match, i)
#     i+=1


# f=866
# print(df.text[f], df.category[f])



n = 65

positive = df[(df.category == 'Positive')].sample(frac=1).reset_index(drop=True)[:n]
negative = df[(df.category == 'Negative')].sample(frac=1).reset_index(drop=True)[:n]
hotline = df[(df.category == 'Hotline')].sample(frac=1).reset_index(drop=True)[:n]
hooligan = df[(df.category == 'Hooligan')].sample(frac=1).reset_index(drop=True)[:n]
siteandcoins = pd.read_csv('data/coins.csv')[:n]

DF = pd.concat([positive, negative, hotline, hooligan, siteandcoins])
DF.to_csv('data/category.csv', index=False)