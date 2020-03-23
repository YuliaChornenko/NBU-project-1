from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import cleaner.TextCleaner as tc
import preparer.TextPreparer as tp
import way
from keras.preprocessing.text import Tokenizer
import numpy as np
from keras.preprocessing import sequence
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

file = '../data/data_nbu.csv'
first = pd.read_csv(file)
second = tc.CleanText.prepare_text(first)
second['category_code'] = second.category.apply(lambda x: 5 if x == 'SiteAndCoins' else 2)
cat_code = second.category_code
desc = second.description

n = len(cat_code)


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



regressor = RandomForestRegressor()
parametrs = {'max_depth': range(1,30)}
grid = GridSearchCV(regressor, parametrs, cv=5)
grid.fit(X_train, y_train)
print(grid)
print(grid.best_params_)
print(grid.best_score_)
print(grid.best_estimator_.alpha)


# regressor.fit(X_train, y_train)
# y_pred = regressor.predict(X_test)
#
# text_labels = encoder.classes_
#
# tokenizer = Tokenizer(num_words=vocab_size)
# tokenizer.fit_on_texts(desc.tolist())
#
# X_test1 = tokenizer.texts_to_sequences(desc.tolist())
# X_test1 = sequence.pad_sequences(X_test1, maxlen=maxSequenceLength)
#
# match = 0
# for i in range(n):
#     prediction = regressor.predict(np.array([X_test1[i]]))
#     predicted_label = text_labels[np.argmax(prediction)]
#     dict_ans = {
#         0:'Positive',
#         1:'Negative',
#         2:'Hotline',
#         3:'Hooligan',
#         4:'Offer',
#         5:'SiteAndCoins'
#     }
#     if predicted_label in dict_ans:
#         predicted_label = dict_ans[predicted_label]
#
#     if cat_code[i] in dict_ans:
#         cat = dict_ans[cat_code[i]]
#
#     if cat == predicted_label:
#         match+=1
#
#     print('========================================')
#     print("Определенная моделью категория: {}".format(predicted_label))
#     print('Правильная категория: {}'.format(cat))
# print('Совпадений: ', match)
#
#
#
