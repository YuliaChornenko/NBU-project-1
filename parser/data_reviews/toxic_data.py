import pandas as pd


fixed_df = pd.read_csv("../../data/labeled.csv", delimiter=',',
                       names=['text', 'toxic'])

new_toxic_list = list()
for ls in fixed_df['toxic']:
    new_toxic_list.append(int(ls))

new_text_list = list()
for ls in fixed_df['text']:
    new_text_list.append(ls)

new_toxic = list()
n = 0
for comments in new_text_list:
    new_toxic.append([new_text_list[n],new_toxic_list[n]])
    n +=1

toxic_list = new_toxic[:200]

for ls in toxic_list:
    if ls[1] == 1:
        ls[1] = 'Hooligan'
    else:
        toxic_list.remove(ls)

for ls in toxic_list:
    if ls[1] == 0 or ls[1] == 1:
        toxic_list.remove(ls)
