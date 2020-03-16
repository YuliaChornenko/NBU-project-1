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
#
#
# df = pd.read_csv('data/data.csv')
# ukr = 0
# rus = 0
# m=0
# d=0
# i = df[(df.category == 'Positive')]
# k = df[(df.category == 'Negative')]
# for line in i.text:
#     if str(detect(line)) == 'uk':
#         ukr +=1
#     elif str(detect(line)) == 'ru':
#         rus +=1
#
# print(ukr,rus)
# from spellchecker import SpellChecker
#
# spell = SpellChecker(language=None, case_sensitive=True)
# spell.word_frequency.load_text_file('ru_full.txt')
# # find those words that may be misspelled
# misspelled = spell.unknown(['привет', 'привит'])
#
# for word in misspelled:
#     # Get the one `most likely` answer
#     print(spell.correction(word))
#
#     # Get a list of `likely` options
#     print(spell.candidates(word))

# from googletrans import Translator
# translator = Translator()
# print(translator.translate('안녕하세요', dest='uk').text)

# from translate import Translator
# translator= Translator(to_lang="uk")
# translation = translator.translate("Блядь ты меня заебал пиздец блин как можно")
# print(translation)

