import pandas as pd

df = pd.read_csv('data/category.csv')
print(df.category.value_counts())
