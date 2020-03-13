import pandas as pd
from parser.data_reviews.pos_and_neg import ReviewsURLScraper
from parser.data_reviews.name_of_pages import banks_url, pos_url, reviews_page, hotlines_page
from parser.data_reviews.toxic_data import toxic_list

reviews_url = ReviewsURLScraper.get_reviews_url(banks_url=banks_url, page=reviews_page)
hotlines_url = ReviewsURLScraper.get_reviews_url(banks_url=banks_url, page=hotlines_page)

reviews_list = ReviewsURLScraper.get_pos_and_neg_reviews(reviews_url=reviews_url)
hotlines_list = ReviewsURLScraper.get_hotlines(hotlines_url=hotlines_url)
positive_list = ReviewsURLScraper.get_positive(pos_url=pos_url)

final_list = positive_list[:20]+reviews_list+hotlines_list+toxic_list

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
df.to_csv('../../data/data.csv', index=False)
