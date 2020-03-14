import pandas as pd
import cleaner.TextCleaner as tc
from way import pickle, rcsv

df = pd.read_csv(rcsv)
df = tc.CleanText.prepare_df(df, pickle=pickle)
