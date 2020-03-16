import pandas as pd
import re
from langdetect import detect
import cleaner.TextCleaner as tc

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

n = 100

positive = tc.CleanText.detect_lang(df, 'Positive', n).sample(frac=1).reset_index(drop=True)
negative = tc.CleanText.detect_lang(df, 'Negative', n).sample(frac=1).reset_index(drop=True)
hotline = tc.CleanText.detect_lang(df, 'Hotline', n).sample(frac=1).reset_index(drop=True)
hooligan = df[(df.category == 'Hooligan')].sample(frac=1).reset_index(drop=True)[:n]
offer = df[(df.category == 'Offer')].sample(frac=1).reset_index(drop=True)[:n]
siteandcoins = pd.read_csv('../data/coins.csv')[:n]

DF = pd.concat([positive, negative, hotline, hooligan, offer, siteandcoins])
DF.to_csv('../data/category.csv', index=False)
