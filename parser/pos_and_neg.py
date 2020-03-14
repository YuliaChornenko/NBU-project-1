from bs4 import BeautifulSoup
import requests as req


class ReviewsURLScraper:
    """
    Parsing positive, negative comments, hotlines from minfin.com.ua and positive comments from about.pumb.ua
    """
    @staticmethod
    def get_reviews_url(banks_url=None, reviews=list(), page=None):
        """
        get list of top 20 banks list from minfin.com.ua
        :param banks_url: link of main page
        :param reviews: new list
        :param page: string
        :return: list of banks links
        """
        resp = req.get(banks_url+'/banks/top/')
        soup = BeautifulSoup(resp.text, 'lxml')
        top_20_banks = soup.find_all('tr')[3:23]
        for bank in top_20_banks:
            link = str(bank.find('a')).split('\"')[1]
            reviews.append(banks_url + link + page)

        return reviews

    @staticmethod
    def get_pos_and_neg_reviews(reviews_url=None, reviews_list=list()):
        """
        parsing list of positive and negative comments
        :param reviews: list of url
        :param reviews_list: new list
        :return: list positive and negative comments
        """
        for url in reviews_url:
            for i in range(1, 2):
                resp2 = req.get(url+str(i))
                soup2 = BeautifulSoup(resp2.text, 'lxml')
                reviews1 = soup2.find_all('div', 'comment')
                for review in reviews1:
                    rating = int(len(review.find_all('div', 'mfb-stars mfb-stars--fill')))
                    if rating <= 3:
                        intonation = 'Negative'
                    else:
                        intonation = 'Positive'
                    text = review.find('div', 'text').text
                    reviews_data = [text, intonation]
                    reviews_list.append(reviews_data)

        return reviews_list

    @staticmethod
    def get_positive(pos_url=None, positive_list=list()):
        """
        parsing list of positive comments
        :param pos_url: only positive comments link
        :param positive_list: new list
        :return: list of positive comments
        """
        resp4 = req.get(pos_url)
        soup4 = BeautifulSoup(resp4.text, 'lxml')
        positive = soup4.find_all('div', 'txt-block')
        for pos in positive:
            pos_reviews = pos.find_all('p')
            for pos_re in pos_reviews[0::3]:
                intonation = 'Positive'
                positive_list.append([pos_re.text, intonation])

        return positive_list

    @staticmethod
    def get_hotlines(hotlines_url=None, hotlines_list=list()):
        """
        parsing list of hotlines
        :param hotlines_url: list of link
        :param hotlines_list: new list
        :return: list of hotlines
        """
        for url in hotlines_url:
            resp3 = req.get(url)
            soup3 = BeautifulSoup(resp3.text, 'lxml')
            hotline = soup3.find_all('div', 'comment')
            for line in hotline:
                question = line.find('div', 'text').text
                intonation = 'Hotline'
                hotline_data = [question, intonation]
                hotlines_list.append(hotline_data)

        return hotlines_list