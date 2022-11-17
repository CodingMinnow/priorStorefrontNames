"""

"""

import re
from urllib.parse import urlparse, parse_qs

def identifyKeyParagraph(soup):
    # second to last paragraph contains prior storefront names
    paragraphs = soup.find_all('p')
    key_para = paragraphs[-2]

    # double check that the paragraph is still key
    # i.e. that there haven't been any changes to the website html layout
    if "For most recent reviews checkout" in key_para.a.previous_sibling.text:
        return(key_para)
    else:
        raise Exception("'For most recent reviews checkout' is not in the key paragraph")

def getPriorNames(key_para):
    key_sentence = str(key_para.a.next_sibling)
    prior_names = []

    # check if prior names exist
    if "Previously" in key_sentence:
        extracted_names = re.search('Previously known as (.*), and have since changed the seller name.', key_sentence).group(1)
        prior_names = extracted_names.split(", ")
    
    return prior_names

def getStorefrontName(key_para):
    key_sentence = str(key_para.a.string)
    return re.search('(.*) profile on Amazon(.*)', key_sentence).group(1)

def getSellerID(key_para):
    # extract the seller ID of the storefront from the amazon url of the storefront
    url = key_para.a.get('href')
    parsed_url = parse_qs(urlparse(url).query)
    return parsed_url['seller'][0]
