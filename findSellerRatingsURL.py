"""
Given an excel file of storefront names and sellerID (columns 1 and 2, respectively),
Creates a new excel file with the SellerRatings URL for each storefront in column 3
"""

from bs4 import BeautifulSoup
import openpyxl
import requests

import datetime
import os

from storefrontPage import identifyKeyParagraph, getStorefrontName, getSellerID, baseURLs

# function that generates possible SellerRatings url paths given a storefront name
def convertStorefrontNameToPath(storefront):
    possible_paths = []
    num_of_hyphens_at_end = 3
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

    return possible_paths


# function that finds the right url by comparing the storefront name to the one in the web page
def getRightPath(storefront, sellerID, paths):
    valid_urls = []
    
    for base in baseURLs:
        for path in paths:
            url = ''.join([base, path])
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                keyPara = identifyKeyParagraph(soup)
                
                # if sellerID matches, found exact match
                if sellerID == getSellerID(keyPara):
                    return url

                # if storefront name matches, move on to next country
                if storefront == getStorefrontName(keyPara):
                    valid_urls.append(url)
                    break
    
    # if one valid url, found exact match
    if len(valid_urls) == 1:
        return valid_urls[0]
    # get user input to select one url
    elif len(valid_urls) > 1:
        userConfirm = ''

        while userConfirm == 'n' or userConfirm == '':
            userInput = ''
            userConfirm = ''
            first_try = True
            first_try_confirm = True
            
            while not userInput.isnumeric() or int(userInput) not in range(len(valid_urls)):
                if first_try:
                    print(f'For the storefront "{storefront}", there are more than one possible urls. They are as follows: ')
                    for idx, valid_url in enumerate(valid_urls):
                        print(f'{idx}: {valid_url}')
                    print('Please review and return the number corresponding to the correct url. If none of them are correct, please type in "none" or "n".')
                else:
                    print('Try again. Your input is invalid.')
                first_try = False
                userInput = input()

            while userConfirm.lower() not in {'y','n'}:
                if first_try_confirm:
                    print(f'You selected {userInput}. If it is correct, please type "y". Else, "n".')
                else:
                    print('Try again. Your input is invalid.')
                first_try_confirm = False
                userConfirm = input()
        
        if userInput.isalpha() and (userInput.lower() == "none" or userInput.lower() == "n"):
            return None
        else:
            return valid_url[userInput]

# load excel
file_path = '../data.xlsx'
workbook = openpyxl.load_workbook(file_path) # Q: should i get the user to specify the spreadsheet?
sheet = workbook.active

# create a column to add urls
sheet.insert_cols(3)
sheet['C1'] = "url"

# find each storefront's url and add to excel
for row_idx in range(2, sheet.max_row+1):
    storefront = sheet.cell(row=row_idx, column=1).value
    sellerID = sheet.cell(row=row_idx, column=2).value
    print(f'storefront: {storefront}')
    possible_paths = convertStorefrontNameToPath(storefront)
    sheet['C'+str(row_idx)] = getRightPath(storefront, sellerID, possible_paths)

# try to save
workbook.save(os.path.splitext(file_path)[0] + " - " + datetime.datetime.now().strftime("%m-%d-%Y %I %M %p") + '.xlsx')
