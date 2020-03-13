import pandas as pd
import cleaner.TextCleaner as tc

df = pd.read_csv('../data/category.csv')
df = tc.CleanText.prepare_df(df)


