"""
Given a list of storefront names, find the associated SellerRatings URL for each
"""

import requests

storefront = "Pattern -iServe-"
sellerID = "A2EJCTH67GJMT3"
url = "https://www.sellerratings.com/amazon/usa/pattern-iserve-"

storefront = [
    "Pattern -iServe-",
    "Tipiliano",
    "KRISHNA ART;",
    "Y2V®",
    "TechTack(EU)",
    "A & A Agencies",
    "A A AGENCIES",
    "A A AGENCIES",
    "Assurant Europe Insurance N.V.",
    "SHIV COLLECTION-",
    "ブックオフオンライン",
    "pets--lover",
    "バリューブックス　　　【防水梱包で、丁寧に発送します】"
]
url = [
    "https://www.sellerratings.com/amazon/usa/pattern-iserve-",
    "https://www.sellerratings.com/amazon/italy/tipiliano",
    "https://www.sellerratings.com/amazon/india/krishna-art-",
    "https://www.sellerratings.com/amazon/india/y2v",
    "https://www.sellerratings.com/amazon/uk/techtackeu",
    "https://www.sellerratings.com/amazon/india/a-a-agencies--",
    "https://www.sellerratings.com/amazon/india/a-a-agencies-",
    "https://www.sellerratings.com/amazon/india/a-a-agencies",
    "https://www.sellerratings.com/amazon/germany/assurant-europe-insurance-nv-",
    "https://www.sellerratings.com/amazon/india/shiv-collection-",
    "https://www.sellerratings.com/amazon/japan/%E3%83%96%E3%83%83%E3%82%AF%E3%82%AA%E3%83%95%E3%82%AA%E3%83%B3%E3%83%A9%E3%82%A4%E3%83%B3",
    "https://www.sellerratings.com/amazon/uk/pets-lover",
    "https://www.sellerratings.com/amazon/japan/%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC%E3%83%96%E3%83%83%E3%82%AF%E3%82%B9-%E9%98%B2%E6%B0%B4%E6%A2%B1%E5%8C%85%E3%81%A7%E4%B8%81%E5%AF%A7%E3%81%AB%E7%99%BA%E9%80%81%E3%81%97%E3%81%BE%E3%81%99"
]
sellerID = [
    "A2EJCTH67GJMT3",
    "AZLMOZ4VFVEK1",
    "A1L2Z4YE59KMJ4",
    "A39DG6UK0UIUH1",
    "A3NULHOW1R9CIG",
    "A1KSQZQJQ8A2Q3",
    "A31XQ1SNFRULPQ",
    "A39L3W0FABL7RL",
    "A2N284U23UVV38",
    "A1NCCEAREVWNUG",
    "ACQ147NXSZMKZ",
    "ABCL8ENSCFGNK",
    "A3BAVLDFUS0PHE"
]

baseURLs = [
    'https://www.sellerratings.com/amazon/usa/',
    'https://www.sellerratings.com/amazon/uk/',
    'https://www.sellerratings.com/amazon/germany/',
    'https://www.sellerratings.com/amazon/france/',
    'https://www.sellerratings.com/amazon/italy/',
    'https://www.sellerratings.com/amazon/spain/',
    'https://www.sellerratings.com/amazon/japan/',
    'https://www.sellerratings.com/amazon/india/'
]

# find possible SellerRatings url syntaxes of storefront
newStorefront = len(storefront)
for char in storefront:
    # hyphen --> space
    if char == chr(45):


# find exact match using name

# find exact match using sellerID


