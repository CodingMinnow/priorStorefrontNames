"""
Scrape all of the storefronts listed in the SellerRatings website (all 2500 for each country)
Store the data (name, seller ID, prior names) to a MySQL database
"""

from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv
import mysql.connector
from mysql.connector import errorcode
import requests

from decouple import config
import logging
import time

from utils.countryPageUtils import *
from utils.storefrontPageUtils import *

# execution time
start_time = time.time()

# configure logging
logging.basicConfig(filename='app.log', format='%(asctime)s - filename: %(filename)s, line: %(levelno)s - %(message)s',  datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

# verify total pages = 26 for each country
for url in base_urls.values():
    if not verifyLastPage(url):
        raise Exception('There have been changes to the number of pages. Update.')

# load environment variables
load_dotenv(find_dotenv())
DB_USER = config('DB_USER', default='')
DB_PASSWORD = config('DB_PASSWORD', default='')

# connect to mysql
config = {
    'user': DB_USER,
    'password': DB_PASSWORD,
    'host': '127.0.0.1',
    'database': 'webscraper',
    'raise_on_warnings': True
}
try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    logging.error(err)
    raise Exception("Couldn't connect to database")
cursor = cnx.cursor()

add_storefront_name = ("INSERT INTO webscraper (SellerID, StorefrontName, NameCurrent, Country) VALUES (%(seller_ID)s, %(storefront_name)s, %(name_current)s, %(country)s, %(storefront_url)s)")

# scrape storefront and its sellerratings url
for country in base_urls:
    # get all 25 pages
    country_pages = []
    for page in range(1,26):
        res_country_page = requests.get(base_urls[country] + '?page=' + str(page))

        # log non-200 status code responses 
        if res_country_page.status_code != 200:
            logging.error(f'Failed to successfully get page {page} of {country}.')
            continue

        country_pages.append(res_country_page.content)

    # scrape each page
    for country_page in country_pages:
        soup_country_page = BeautifulSoup(country_page, "html.parser")
        table = soup_country_page.find(id='report')
        table_body = table.find('tbody')
        row = table_body.find('tr')

        # iterate through storefronts on this page
        while row is not None:
            key_excerpt = row.find('a')
            storefront = key_excerpt.text
            url = key_excerpt.get('href')

            # get storefront sellerratings page
            sellerRatings_URL = 'https://www.sellerratings.com/' + url
            res_sf = requests.get(sellerRatings_URL)
            
            # log non-200 status code
            if res_sf.status_code != 200:
                logging.error(f'Failed to successfully get the sellerratings page of storefront {storefront} in country {country}. The attempted url path was {url}.')
                continue

            # scrape the sellerID and prior names
            soup_sf = BeautifulSoup(res_sf.content, "html.parser")
            key_para = identifyKeyParagraph(soup_sf)
            seller_ID = getSellerID(key_para)
            prior_names = getPriorNames(key_para)

            # insert current and outdated storefront names into database
            storefront_data = {
                'seller_ID': seller_ID,
                'storefront_name': storefront,
                'name_current': 1,
                'country': country,
                'storefront_url': url
            }
            cursor.execute(add_storefront_name, storefront_data)

            for prior_name in prior_names:
                prior_name_data = {
                    'seller_ID': seller_ID,
                    'storefront_name': prior_name,
                    'name_current': 0,
                    'country': country
                }
                cursor.execute(add_storefront_name, prior_name_data)
            
            row = row.next_sibling.next_sibling

# mysql
cnx.commit()
cursor.close()
cnx.close()

# execution time
end_time = time.time()
logging.info(f"Total runtime of the program is {(end_time - start_time)/60} minutes.")
