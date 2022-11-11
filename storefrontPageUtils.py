import re
from urllib.parse import urlparse, parse_qs

def identifyKeyParagraph(soup):
    # second to last paragraph contains prior storefront names
    paragraphs = soup.find_all('p')
    keyPara = paragraphs[-2]

    # double check that the paragraph is still key
    if "For most recent reviews checkout" in keyPara.a.previous_sibling.text:
        return(keyPara)
    else:
        raise Exception("'For most recent reviews checkout' is not in the key paragraph")

def getPriorNames(keyPara):
    keySentence = str(keyPara.a.next_sibling)
    priorNames = []

    # check if prior names exist
    if "Previously" in keySentence:
        extractedNames = re.search('Previously known as (.*), and have since changed the seller name.', keySentence).group(1)
        priorNames = extractedNames.split(", ")
    
    return priorNames

def getStorefrontName(keyPara):
    keySentence = str(keyPara.a.string)
    return re.search('(.*) profile on Amazon(.*)', keySentence).group(1)

def getSellerID(keyPara):
    # extract the seller ID of the storefront from the amazon url of the storefront
    url = keyPara.a.get('href')
    sellerRatingsSellerID = parse_qs(urlparse(url).query)
    return sellerRatingsSellerID['seller'][0]
