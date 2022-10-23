from bs4 import BeautifulSoup
import requests

from storefrontPage import identifyKeyParagraph, verifySellerId, scrapePriorNames

# data for testing
url = "https://www.sellerratings.com/amazon/usa/pattern-iserve-"
sellerID = "A2EJCTH67GJMT3"
# url = "https://www.sellerratings.com/amazon/italy/tipiliano"
# sellerID = "AZLMOZ4VFVEK1"

def priorNamesAmazonSF(url, sellerID):
    # get storefront sellerratings page
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, "html.parser")
    keyPara = identifyKeyParagraph(soup)
        
    if verifySellerId(keyPara, sellerID):
        return scrapePriorNames(keyPara)
    else:
        raise Exception("Mismatch in seller ID and SellerRatings url")

priorNamesAmazonSF(url, sellerID)
