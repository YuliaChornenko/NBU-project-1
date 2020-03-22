import pandas as pd
import cleaner.TextCleaner as tc

df = pd.read_csv('../data/data.csv')

df.drop(df[(df.category == '1') | (df.category == '0')].index, inplace=True)

n = 100
# half = int(n/2)

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

# positive = tc.CleanText.detect_lang(df, 'Positive', n)
# positive_uk = positive[:half]
# positive_rus = positive[half:]
# negative = tc.CleanText.detect_lang(df, 'Negative', n)
# negative_uk = negative[:half]
# negative_rus = negative[half:]
# hotline = tc.CleanText.detect_lang(df, 'Hotline', n)
# hotline_uk = hotline[:half]
# hotline_rus = hotline[half:]
# hooligan = df[(df.category == 'Hooligan')].sample(frac=1).reset_index(drop=True)[:n]
# offer = df[(df.category == 'Offer')].sample(frac=1).reset_index(drop=True)[:n]
#
# siteandcoins1 = tc.CleanText.detect_lang(df, 'SiteAndCoins', 62)
# siteandcoins1_uk = siteandcoins1[:30]
# siteandcoins1_rus = siteandcoins1[31:]
# siteandcoins2 = pd.read_csv('../data/coins.csv')
# siteandcoins = pd.concat([siteandcoins1, siteandcoins2])[:n]
#
# df_test = pd.concat([positive_uk[:10], positive_rus[:10], negative_uk[:10], negative_rus[:10], hotline_uk[40:], hotline_rus[40:],
#                      hooligan[:20], offer[:20], siteandcoins2[20:40]]).to_csv('../data/df_test.csv')
#
# df_train = pd.concat([positive_uk[10:], positive_rus[10:], negative_uk[10:], negative_rus[10:], hotline_uk[:40], hotline_rus[:40],
#                       hooligan[20:], offer[20:], siteandcoins1_uk, siteandcoins1_rus, siteandcoins2[:19]]).to_csv('../data/df_train.csv')
