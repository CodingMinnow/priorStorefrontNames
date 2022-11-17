"""

"""

import requests

base_urls = {
    'usa' : 'https://www.sellerratings.com/amazon/usa',
    'uk' : 'https://www.sellerratings.com/amazon/uk',
    'germany' : 'https://www.sellerratings.com/amazon/germany',
    'france' : 'https://www.sellerratings.com/amazon/france',
    'italy' : 'https://www.sellerratings.com/amazon/italy',
    'spain' : 'https://www.sellerratings.com/amazon/spain',
    # 'japan' : 'https://www.sellerratings.com/amazon/japan',
    'india' : 'https://www.sellerratings.com/amazon/india'
}

def verifyLastPage(country_url):
    # last page should exist
    response = requests.get(country_url + '?page=25')
    last_page = response.status_code == 200

    # page after last shouldn't exist
    response_two = requests.get(country_url + '?page=26')
    page_after_last = response_two.status_code == 404

    return last_page and page_after_last


# def findLastPage(country_url):
#     lower_bound = 1
#     upper_bound = 25
#     middle = (upper_bound - lower_bound)//2
#     response = requests.get(country_url + '?page=' + upper_bound)
#     response.raise_for_status()
#     print(response.status_code)
#     print(response.content)
