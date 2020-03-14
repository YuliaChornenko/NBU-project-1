import pandas as pd
from parser.pos_and_neg import ReviewsURLScraper
from parser.toxic_data import ToxicComments
from parser.name_of_pages import banks_url, pos_url, reviews_page, hotlines_page, file_name

reviews_url = ReviewsURLScraper.get_reviews_url(banks_url=banks_url, page=reviews_page)
hotlines_url = ReviewsURLScraper.get_reviews_url(banks_url=banks_url, page=hotlines_page)

reviews_list = ReviewsURLScraper.get_pos_and_neg_reviews(reviews_url=reviews_url)
hotlines_list = ReviewsURLScraper.get_hotlines(hotlines_url=hotlines_url)
positive_list = ReviewsURLScraper.get_positive(pos_url=pos_url)

fixed_df = ToxicComments.read_file(file_name)
new_toxic_list = ToxicComments.create_toxic_list(fixed_df=fixed_df)
new_text_list = ToxicComments.create_text_list(fixed_df=fixed_df)
toxic_list = ToxicComments.create_final_toxic(new_text_list=new_text_list, new_toxic_list=new_toxic_list)

final_list = positive_list[:22]+reviews_list+hotlines_list+toxic_list

text_list = list()
for ls in final_list:
    text_list.append(ls[0])

intonation_list = list()
for ls in final_list:
    intonation_list.append(ls[1])


df = pd.DataFrame({'text': text_list,
                    'category': intonation_list})

compression_opts = dict(method='zip',
                     archive_name='data.csv')
df.to_csv('../data/data.csv', index=False)
