import pymorphy2
import re
import pandas as pd

class CleanText:

    @staticmethod
    def clean_text(text):
        '''
        Clean text

        :param text: text to clean
        :return: clean text
        '''

        ma = pymorphy2.MorphAnalyzer()

        text = str(text).lower()
        text = re.sub('\-\s\r\n\s{1,}|\-\s\r\n|\r\n', '', text)
        text = re.sub('[.,:;_%©?*,!@#$%^&()]|[+=]|[]]|[/]|"|\s{2,}|-', ' ', text)
        text = " ".join(ma.parse(word)[0].normal_form for word in text.split())
        text = ' '.join(word for word in text.split() if len(word) > 3)

        return text

    @staticmethod
    def prepare_text(df):
        '''
        Create new column in DataFrame with clean text(using function 'clean_text')

        :param df: DataFrame which consist of the text to be cleaned
        :return: DataFrame with new column of cleaned text
        '''

        df['description'] = df.apply(lambda x: CleanText.clean_text(x['text']), axis=1)

        return df

    @staticmethod
    def clean_category(df):
        '''
        Replace categories with numbers

        :param df: DataFrame with categories
        :return: DataFrame with new column of replaced categories
        '''

        categories = {}
        for key, value in enumerate(df['category'].unique()):
            categories[value] = key

        df['category_code'] = df['category'].map(categories)

        total_categories = len(df['category'].unique())
        print('Total categories: {}'.format(total_categories))

        return df

    @staticmethod
    def prepare_df(df):
        '''
        Create new DataFrame with cleaned text and replaced categories (using functions 'clean_category' and 'prepare_text')

        :param df: Default DataFrame
        :return: New DataFrame with clean text and replaced categories
        '''

        if 'category_code' not in df.columns:
            df = CleanText.clean_category(df)
        c_text = CleanText.prepare_text(df)
        df.to_pickle('data/dataframe.pkl')
        df_new = pd.read_pickle('data/dataframe.pkl')

        return df_new

    # def open_file(file):
    #     list_text = []
    #     with open(file, encoding='utf-8') as f:
    #         for line in f:
    #             if line.strip().split(' ') == ['']:
    #                 continue
    #             match = re.findall(r'[\*]{3}(\w+)[\*]{3}', line)
    #             new_line = ' '.join(line.strip().split(' '))
    #             text = re.sub('\n', '', new_line)
    #             print(match)
    #             list_text.append([text])
    #     print(list_text)
