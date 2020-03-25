import pandas as pd
import numpy as np
import way
import preparer.TextPreparer as tp
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM

df = pd.read_pickle(way.pickle)
df = df.sample(frac=1).reset_index(drop=True)
categories = df.category_code
descriptions = df.description
text = df.text

tokenizer, textSequences = tp.PrepareText.tokenizer(descriptions)
X_train, y_train, X_test, y_test = tp.PrepareText.load_data_from_arrays(descriptions, categories, train_test_split=0.8)

X_train_n, y_train_n, X_test_n,  y_test_n = tp.PrepareText.load_data_from_arrays(text, categories, train_test_split=0.8)

test_df = (pd.DataFrame({'text':list(X_test_n),
                       'category': list(y_test_n)})).to_csv('data/out_test_data.csv', index=False)
n = len(y_test_n)

total_unique_words, maxSequenceLength = tp.PrepareText.max_count(descriptions, tokenizer)
vocab_size = round(total_unique_words/10)

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
batch_size = 64
epochs = 8

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

model.save('model/save/model(our test data).h5')

text_labels = encoder.classes_

match = 0
for i in range(n):
    prediction = model.predict(np.array([X_test[i]]))
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

    if list(y_test[i]).index(1) in dict_ans:
        cat = dict_ans[list(y_test[i]).index(1)]

    if cat == predicted_label:
        match += 1

    print('========================================')
    print("Определенная моделью категория: {}".format(predicted_label))
    print('Правильная категория: {}'.format(cat))
print('Совпадений: ', match)


