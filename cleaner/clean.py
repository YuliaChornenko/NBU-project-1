import pandas as pd
import cleaner.TextCleaner as tc

df = pd.read_csv('../data/data.csv')

df.drop(df[(df.category == '1') | (df.category == '0')].index, inplace=True)

n = 100

positive = tc.CleanText.detect_lang(df, 'Positive', n).sample(frac=1).reset_index(drop=True)
negative = tc.CleanText.detect_lang(df, 'Negative', n).sample(frac=1).reset_index(drop=True)
hotline = tc.CleanText.detect_lang(df, 'Hotline', n)
hooligan = df[(df.category == 'Hooligan')].sample(frac=1).reset_index(drop=True)[:n]
offer = df[(df.category == 'Offer')].sample(frac=1).reset_index(drop=True)[:n]
siteandcoins1 = tc.CleanText.detect_lang(df, 'SiteAndCoins', 62)
siteandcoins2 = pd.read_csv('../data/coins.csv')
siteandcoins = pd.concat([siteandcoins1, siteandcoins2])[:n]

DF = pd.concat([positive, negative, hotline, hooligan, offer, siteandcoins])
DF.to_csv('../data/category.csv', index=False)
