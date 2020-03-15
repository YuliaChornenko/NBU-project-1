import pandas as pd
import cleaner.TextCleaner as tc
from langdetect import detect
import pymorphy2

str1 = "як умру то поховайте"
lang = str(detect("як умру то поховайте"))
morph = pymorphy2.MorphAnalyzer(lang=lang)
print(morph.parse(str1))

# df = pd.read_pickle('data/dataframe.pkl')
# n = 1
# print(df.description[n], '\n', df.category[n])
#
# file = 'data/letters1.txt'
# tc.CleanText.open_file(file)

