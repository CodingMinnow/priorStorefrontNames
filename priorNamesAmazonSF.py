"""
"""

from bs4 import BeautifulSoup
import requests

from utils.storefrontPageUtils import identifyKeyParagraph, getSellerID, getPriorNames

# data for testing
url = "https://www.sellerratings.com/amazon/usa/pattern-iserve-"
seller_ID = "A2EJCTH67GJMT3"
# url = "https://www.sellerratings.com/amazon/italy/tipiliano"
# seller_ID = "AZLMOZ4VFVEK1"

# returns a dictionary 
def priorNamesAmazonSF(url, seller_ID = None):
    # get storefront sellerratings page
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, "html.parser")
    key_para = identifyKeyParagraph(soup)
        
    # even if no seller_ID is given, look for prior names (just know that there's a chance the url may not be the right one for the storefront)
    if seller_ID is None or seller_ID == getSellerID(key_para):
        return getPriorNames(key_para)
    
    raise Exception("Mismatch in seller ID and SellerRatings url")

# priorNamesAmazonSF(url, seller_ID)
