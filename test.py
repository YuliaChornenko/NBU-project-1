import pandas as pd
import cleaner.TextCleaner as tc

# df = pd.read_pickle('data/dataframe.pkl')
# n = 1
# print(df.description[n], '\n', df.category[n])

file = 'data/letters1.txt'
tc.CleanText.open_file(file)