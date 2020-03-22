import pandas as pd
import numpy as np
import way
import cleaner.TextCleaner as tc
import preparer.TextPreparer as tp
from keras.models import Sequential
from keras.preprocessing import sequence
from keras.layers import Dense, Embedding, LSTM
from keras.preprocessing.text import Tokenizer

file = 'data/data_nbu.csv'
first = pd.read_csv(file)
second = tc.CleanText.prepare_text(first)
second['category_code'] = second.category.apply(lambda x: 5 if x == 'SiteAndCoins' else 2)
cat_code = second.category_code
desc = second.description


# all = pd.read_csv('data/category.csv')
# descriptions = tc.CleanText.prepare_text(all).description
# tokenizer, textSequences = tp.PrepareText.tokenizer(descriptions)

# train = pd.read_pickle('data/df_train.pkl')
# X_train = train.description
# y_train = train.category_code
# test = pd.read_pickle('data/df_test.pkl')
# X_test = test.description
# y_test = test.category_code

n = len(all.category)


df = pd.read_pickle(way.pickle)
df = df.sample(frac=1).reset_index(drop=True)
categories = df.category_code
descriptions = df.description

tokenizer, textSequences = tp.PrepareText.tokenizer(descriptions)
print(textSequences)
X_train, y_train, X_test, y_test = tp.PrepareText.load_data_from_arrays(descriptions, categories, train_test_split=0.8)

total_unique_words, maxSequenceLength = tp.PrepareText.max_count(descriptions, tokenizer)
vocab_size = round(total_unique_words/10)
print(maxSequenceLength)

encoder, num_classes = tp.PrepareText.num_classes(y_train, y_test)


X_train, X_test, y_train, y_test = tp.PrepareText.transform_sets(vocab_size, descriptions ,X_train, X_test, y_train, y_test, maxSequenceLength, num_classes)


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
batch_size = 60
epochs = 1

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

model.save('model/save/model(nbu test data with answ).h5')

text_labels = encoder.classes_

tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(desc.tolist())

X_test1 = tokenizer.texts_to_sequences(desc.tolist())
X_test1 = sequence.pad_sequences(X_test1, maxlen=maxSequenceLength)

match = 0
for i in range(n):
    prediction = model.predict(np.array([X_test1[i]]))
    predicted_label = text_labels[np.argmax(prediction)]
    dict_ans = {
        0:'Positive',
        1:'Negative',
        2:'Hotline',
        3:'Hooligan',
        4:'Offer',
        5:'SiteAndCoins'
    }
    if predicted_label in dict_ans:
        predicted_label = dict_ans[predicted_label]

    if cat_code[i] in dict_ans:
        cat = dict_ans[cat_code[i]]

    if cat == predicted_label:
        match+=1

    print('========================================')
    print("Определенная моделью категория: {}".format(predicted_label))
    print('Правильная категория: {}'.format(cat))
print('Совпадений: ', match)



