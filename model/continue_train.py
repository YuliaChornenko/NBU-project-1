import pandas as pd
import numpy as np
import keras
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
import cleaner.TextCleaner as tc
import preparer.TextPreparer as tp

text = str(input('TEXT: '))
# text1 = str(input('TEXT: '))
# text2 = str(input('TEXT: '))
# text3 = str(input('TEXT: '))
# text4 = str(input('TEXT: '))
# text5 = str(input('TEXT: '))
model = load_model('../model/save/model(nbu test data with answ).h5')
df = pd.DataFrame({'text':[text]})

X_train = df.text
cat = '../data/category_with_received_data.csv'
all = pd.read_csv(cat)
cat = tc.CleanText.clean_category(all)
descriptions = tc.CleanText.prepare_text(all).description

maxSequenceLength, vocab_size, encoder, num_classes = tp.PrepareText.parameters(cat)

tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(descriptions)

X_train = tokenizer.texts_to_sequences(X_train)

X_train = sequence.pad_sequences(X_train, maxlen=maxSequenceLength)

model.predict(X_train)#TODO !!!!!!!!!!!!!!!!!!!

text_labels = encoder.classes_

prediction = model.predict([X_train])
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
print(predicted_label)

ans = input('Модель правильно определила категорию?(y/n): ')
if ans == 'n':
    category = str(input('CATEGORY: '))
    df = pd.DataFrame({'text':[text],
                       'category': [category]})
    cat = '../data/category_with_received_data.csv'
    with open(cat, 'a') as f:
        f.write('"{}",{}\n'.format(text,category))

    #y_train = keras.utils.to_categorical(y_train, num_classes)
    dict_changes = {
        'Positive': np.array([1., 0., 0., 0., 0., 0.]),
        'Negative': np.array([0., 1., 0., 0., 0., 0.]),
        'Hotline': np.array([0., 0., 1., 0., 0., 0.]),
        'Hooligan': np.array([0., 0., 0., 1., 0., 0.]),
        'Offer': np.array([0., 0., 0., 0., 1., 0.]),
        'SiteAndCoins': np.array([0., 0., 0., 0., 0., 1.]),
    }

    y_train = dict_changes[category]
    model.fit(X_train, y_train)
