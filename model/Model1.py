from sklearn.metrics import confusion_matrix
import preparer.TextPreparer as tp
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
import matplotlib.pyplot as plt
import numpy as np
import way
from model.visualization import graphs as gr

descriptions = pd.read_csv('../data/category.csv')
tokenizer, textSequences = tp.PrepareText.tokenizer(descriptions)

train = pd.read_pickle('../data/df_train.pkl')
X_train = train.descriptions
y_train = train.category_code
test = pd.read_pickle('../data/df_test.pkl')
X_test = test.descriptions
y_test = test.category_code

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

for i in range(20):
    prediction = model.predict(np.array([X_test[i]]))
    predicted_label = text_labels[np.argmax(prediction)]
    print('====================================')
    print('Правильная категория: {}'.format(y_test[i]))
    print("Определенная моделью категория: {}".format(predicted_label))


