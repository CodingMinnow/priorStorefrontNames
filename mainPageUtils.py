"""

"""

from itertools import count
from bs4 import BeautifulSoup
import requests

baseURLs = [
    'https://www.sellerratings.com/amazon/usa',
    'https://www.sellerratings.com/amazon/uk',
    'https://www.sellerratings.com/amazon/germany',
    'https://www.sellerratings.com/amazon/france',
    'https://www.sellerratings.com/amazon/italy',
    'https://www.sellerratings.com/amazon/spain',
    # 'https://www.sellerratings.com/amazon/japan',
    'https://www.sellerratings.com/amazon/india'
]

def verifyLastPage(country_url):
    # last page should exist
    response = requests.get(country_url + '?page=25')
    lastPage = response.status_code == 200

    # page after last shouldn't exist
    responseTwo = requests.get(country_url + '?page=26')
    pageAfterLast = responseTwo.status_code == 404

    return lastPage and pageAfterLast


# def findLastPage(country_url):
#     lowerBound = 1
#     upperBound = 25
#     middle = (upperBound - lowerBound)//2
#     response = requests.get(country_url + '?page=' + upperBound)
#     response.raise_for_status()
#     print(response.status_code)
#     print(response.content)
