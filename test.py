import pandas as pd
from keras.preprocessing import sequence
from langdetect import detect
from sklearn.metrics import confusion_matrix
import preparer.TextPreparer as tp
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
import matplotlib.pyplot as plt
import numpy as np
import way
from model.visualization import graphs as gr
import cleaner.TextCleaner as tc
from keras.preprocessing.text import Tokenizer

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

file = 'data/letters1.txt'
a = tc.CleanText.open_file(file)
b = tc.CleanText.prepare_text(a)
print(b)

df = pd.read_pickle(way.pickle)
df = df.sample(frac=1).reset_index(drop=True)
categories = df.category_code
descriptions = df.description

tokenizer, textSequences = tp.PrepareText.tokenizer(descriptions)
X_train, y_train, X_test, y_test = tp.PrepareText.load_data_from_arrays(descriptions, categories, train_test_split=0.8)

total_unique_words, maxSequenceLength = tp.PrepareText.max_count(descriptions, tokenizer)
vocab_size = round(total_unique_words/10)

encoder, num_classes = tp.PrepareText.num_classes(y_train, y_test)


X_train, X_test, y_train, y_test = tp.PrepareText.transform_sets(vocab_size, descriptions ,X_train, X_test, y_train, y_test, maxSequenceLength, num_classes)






X_test1 = b.description

tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(descriptions)

X_test1 = tokenizer.texts_to_sequences(X_test1)
X_test1 = sequence.pad_sequences(X_test1, maxlen=maxSequenceLength)






# максимальное количество слов для анализа
max_features = vocab_size

print('Собираем модель...')
model = Sequential()
model.add(Embedding(max_features, maxSequenceLength))
model.add(LSTM(32, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(num_classes, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print(model.summary())

# обучаем
batch_size = 16
epochs = 11

print('Тренируем модель...')
history = model.fit(X_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(X_test, y_test))

#сравниваем результаты
score = model.evaluate(X_test, y_test,
                       batch_size=batch_size, verbose=1)

print()
print(u'Оценка теста: {}'.format(score[0]))
print(u'Оценка точности модели: {}'.format(score[1]))

text_labels = encoder.classes_

for i in range(120):
    prediction = model.predict(np.array([X_test1[i]]))
    predicted_label = text_labels[np.argmax(prediction)]
    print('====================================')
    print("Определенная моделью категория: {}".format(predicted_label))


y_softmax = model.predict(X_test)




