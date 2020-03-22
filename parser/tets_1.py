import pandas as pd

file_name = '../data/data_nbu1.csv'
fixed_df = pd.read_csv(file_name, delimiter=',',
                               names=['text', 'intonation'])

new_text_list = list()
for ls in fixed_df['text']:
    new_text_list.append(ls)

new_intonation_list = list()
for ls in fixed_df['intonation']:
    new_intonation_list.append(ls)

new_toxic = list()
n = 0
for comments in new_text_list:
    new_toxic.append([new_text_list[n], new_intonation_list[n]])
    n += 1

n=0
#print(len(new_text_list))
for ls in new_toxic:
    if ls[1] == 'SiteAndCoins':
        n += 1
print(n)
