import pandas as pd
import requests as req
from bs4 import BeautifulSoup
import re


class GetOffers:

    @staticmethod
    def get_offers_1(link=None, offers_list=list()):
        """

        :param link: site with offers
        :param offers_list: empty list
        :return: list of offers
        """
        for i in range(1, 5):
           resp = req.get(link + str(i))
           soup = BeautifulSoup(resp.text, 'lxml')
           offers = soup.find_all('div', 'idea-post-content')
           for off in offers:
               offer = re.sub(r'\s+', ' ', (off.text))
               category = 'Offer'
               offers_data = [offer, category]
               offers_list.append(offers_data)

        return offers_list

    @staticmethod
    def get_offers_2(link=None, offers_list=list()):
        """

        :param link: site with offers
        :param offers_list: empty list
        :return: list of offers
        """
        resp = req.get(link)
        soup = BeautifulSoup(resp.text, 'lxml')
        offers = soup.find_all('p')
        for of in offers[3:42]:
            of = of.text
            category = 'Offer'
            new_offers = [of, category]
            offers_list.append(new_offers)

        return offers_list
