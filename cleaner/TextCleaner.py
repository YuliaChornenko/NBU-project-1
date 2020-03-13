import re
import pandas as pd
import pymorphy2
from nltk.corpus import stopwords
import users_stopwords

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
        text = ' '.join([word for word in text.split() if word not in stopwords.words('russian')])
        text = ' '.join([word for word in text.split() if word not in users_stopwords.uk_stopwords])
        text = re.sub('\-\s\r\n\s{1,}|\-\s\r\n|\r\n', '', text)
        text = re.sub('[.,:;_%©№?*,!@#$%^&()\d]|[+=]|[\[][]]|[/]|"|\s{2,}|-', ' ', text)
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

    @staticmethod
    def open_file(file):
        '''
        Read file and create DataFrame

        :param file: File which will be read
        :return: DataFrame with file entries
        '''

        text = []
        list_text = []
        with open(file, encoding='utf-8') as f:
            f = f.readlines()
            print(f)
            for sentence in f:
                if sentence != '***\n':
                    sentence = re.sub('\n', '', sentence)
                    text.append(sentence)
                else:
                    list_text.append([' '.join(text)])
                    text = []

        df = pd.DataFrame(list_text)

        return df

