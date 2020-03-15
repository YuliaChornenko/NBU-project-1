import pandas as pd
from langdetect import detect

import cleaner.TextCleaner as tc

# df = pd.read_pickle('data/dataframe.pkl')
# n=248
# print(df.text[n], df.category_code[n], df.category[n])
# print(df.description[n])

# file = 'data/letters1.txt'
# tc.CleanText.open_file(file)

# from langdetect import detect
# import pymorphy2
#
# str1 = "як умру то поховайте"
# lang = str(detect("як умру то поховайте"))
# morph = pymorphy2.MorphAnalyzer(lang=lang)
# print(morph.parse(str1))


df = pd.read_csv('data/data.csv')
ukr = 0
rus = 0
m=0
d=0
i = df[(df.category == 'Positive')]
k = df[(df.category == 'Negative')]
for line in i.text:
    if str(detect(line)) == 'uk':
        ukr +=1
    elif str(detect(line)) == 'ru':
        rus +=1

print(ukr,rus)
