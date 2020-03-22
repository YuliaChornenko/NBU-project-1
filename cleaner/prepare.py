import pandas as pd
import cleaner.TextCleaner as tc
from way import pickle, rcsv

df = pd.read_csv(rcsv)
df = tc.CleanText.prepare_df(df, pickle=pickle)

# df_test = pd.read_csv('../data/df_test.csv')
# df_test = tc.CleanText.prepare_df(df_test, pickle='../data/df_test.pkl')
#
# df_train = pd.read_csv('../data/df_train.csv')
# df_train = tc.CleanText.prepare_df(df_train, pickle='../data/df_train.pkl')
