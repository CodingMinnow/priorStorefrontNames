"""

"""

from bs4 import BeautifulSoup
import requests

from mainPageUtils import *


# confirm total pages in each country page
for url in baseURLs:
    if not verifyLastPage(url):
        raise Exception('There have been changes to the number of pages. Update.')

