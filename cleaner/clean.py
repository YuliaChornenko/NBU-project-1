import pandas as pd
import re
from langdetect import detect

df = pd.read_csv('../data/data.csv')

df.drop(df[(df.category == '1') | (df.category == '0')].index, inplace=True)

# i = 0
# for line in df.text:
#     match = re.search('[?]', line)
#     try:
#         match = re.search('[?]', line)
#         if (df.category[i] == 'Positive' or df.category[i] == 'Negative') and match != None :
#             df.drop(df.index[i])
#     except:
#         continue
#
#     i += 1

# ukr = 0
# rus = 0
# i = df[(df.category == 'Positive')]
# k = df[(df.category == 'Negative')]
# for line in i.text:
#     if str(detect(line)) == 'uk':
#         ukr +=1
#     elif str(detect(line)) == 'ru':
#         rus +=1
#
# print(ukr,rus)
n = 100

positive = df[(df.category == 'Positive')].sample(frac=1).reset_index(drop=True)[:n]
negative = df[(df.category == 'Negative')].sample(frac=1).reset_index(drop=True)[:n]
hotline = df[(df.category == 'Hotline')].sample(frac=1).reset_index(drop=True)[:n]
hooligan = df[(df.category == 'Hooligan')].sample(frac=1).reset_index(drop=True)[:n]
offer = df[(df.category == 'Offer')].sample(frac=1).reset_index(drop=True)[:n]
siteandcoins = pd.read_csv('../data/coins.csv')[:n]

DF = pd.concat([positive, negative, hotline, hooligan, offer, siteandcoins])
DF.to_csv('../data/category.csv', index=False)
