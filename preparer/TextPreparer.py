import pandas as pd
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from tensorflow import keras
import numpy as np
from sklearn.preprocessing import LabelEncoder

class PrepareText:

    @staticmethod
    def tokenizer(descriptions):

        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(descriptions.tolist())
        textSequences = tokenizer.texts_to_sequences(descriptions.tolist())

        return tokenizer, textSequences

    @staticmethod
    def max_count(descriptions, tokenizer):
        max_words = 0
        for desc in descriptions.tolist():
            words = len(desc.split())
            if words > max_words:
                max_words = words
        print('Максимальное количество слов в самом длинном описании заявки: {} слов'.format(max_words))

        total_unique_words = len(tokenizer.word_counts)
        print('Всего уникальных слов в словаре: {}'.format(total_unique_words))

        maxSequenceLength = max_words

        return total_unique_words, maxSequenceLength

    @staticmethod
    def num_classes(y_train, y_test):
        encoder = LabelEncoder()
        encoder.fit(y_train)
        y_train = encoder.transform(y_train)
        y_test = encoder.transform(y_test)

        num_classes = np.max(y_train) + 1

        print('Количество категорий для классификации: {}'.format(num_classes))

        return encoder, num_classes

    @staticmethod
    def load_data_from_arrays(strings, labels, train_test_split=0.8):
        data_size = len(strings)
        test_size = int(data_size - round(data_size * train_test_split))
        print("Test size: {}".format(test_size))

        print("\nTraining set:")
        x_train = strings[test_size:]
        print("\t - x_train: {}".format(len(x_train)))
        y_train = labels[test_size:]
        print("\t - y_train: {}".format(len(y_train)))

        print("\nTesting set:")
        x_test = strings[:test_size]
        print("\t - x_test: {}".format(len(x_test)))
        y_test = labels[:test_size]
        print("\t - y_test: {}".format(len(y_test)))

        return x_train, y_train, x_test, y_test

    @staticmethod
    def transform_sets(vocab_size, descriptions, X_train, X_test, y_train, y_test, maxSequenceLength, num_classes):
        print('Преобразуем описания заявок в векторы чисел...')
        tokenizer = Tokenizer(num_words=vocab_size)
        tokenizer.fit_on_texts(descriptions)

        X_train = tokenizer.texts_to_sequences(X_train)
        X_test = tokenizer.texts_to_sequences(X_test)

        X_train = sequence.pad_sequences(X_train, maxlen=maxSequenceLength)
        X_test = sequence.pad_sequences(X_test, maxlen=maxSequenceLength)

        print('Размерность X_train:', X_train.shape)
        print('Размерность X_test:', X_test.shape)

        print(u'Преобразуем категории в матрицу двоичных чисел '
              u'(для использования categorical_crossentropy)')
        y_train = keras.utils.to_categorical(y_train, num_classes)
        y_test = keras.utils.to_categorical(y_test, num_classes)
        print('y_train shape:', y_train.shape)
        print('y_test shape:', y_test.shape)

        return X_train, X_test, y_train, y_test
