"""
Given a list of storefront names, find the associated SellerRatings URL for each
"""

import requests

# data for testing
# storefront = "Pattern -iServe-"
# sellerID = "A2EJCTH67GJMT3"
# url = "https://www.sellerratings.com/amazon/usa/pattern-iserve-"

storefronts = [
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
urls = [
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
sellerIDs = [
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

# find possible SellerRatings url paths
possible_paths_dict = {}
for storefront in storefronts:
    possible_paths = []
    num_of_hyphens_at_end = 5
    new_name = [''] * (len(storefront) + num_of_hyphens_at_end)
    pointer = 0

    for idx, char in enumerate(storefront):
        # leave alone if alphabet or number
        if char.isalpha() or char.isnumeric():
            new_name[pointer] = char.lower()
            pointer += 1
        else:
            # leave alone if hyphen is the last character (unless the prior character was non-alphabet or and non-number)
            if idx == len(storefront) - 1 and char == '-' and new_name[pointer - 1] != '-':
                new_name[pointer] = '-'
                pointer += 1
            # replace consecutive spaces and/or hyphens with a single hyphen
            elif char == '-' or char == ' ':
                if new_name[pointer - 1].isalpha() or new_name[pointer - 1].isnumeric():
                    new_name[pointer] = '-'
                    pointer += 1
            # ignore consecutive non-alphabets and non-numbers

    possible_paths.append(''.join(new_name))

    for num in range(num_of_hyphens_at_end):
        new_name[pointer + num] = '-'
        possible_paths.append(''.join(new_name))

    possible_paths_dict[storefront] = possible_paths


# find the right url by comparing the storefront name to the one in the web page
# for base in baseURLs:
#     for storefront in possible_paths_dict:
#         for path in possible_paths_dict[storefront]:
#             url = ''.join([base, path])
#             print(url)
#             response = requests.get(url)
#             response.raise_for_status()
#             print(response)

# verify url using sellerID

# ask for user input

# return findings
