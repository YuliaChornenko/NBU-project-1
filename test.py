import pandas as pd
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
import keras
import cleaner.TextCleaner as tc

X_train = 'дякувати сподобатись'
y_train = 0

model = load_model('model/save/model(nbu test data with answ).h5')
all = pd.read_csv('data/category.csv')
descriptions = tc.CleanText.prepare_text(all).description
vocab_size = 658
maxSequenceLength = 856
num_classes = 6
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(descriptions)

X_train = tokenizer.texts_to_sequences(X_train)

X_train = sequence.pad_sequences(X_train, maxlen=maxSequenceLength)

y_train = keras.utils.to_categorical(y_train, num_classes)

print(X_train.shape)
model.fit(X_train, y_train)
