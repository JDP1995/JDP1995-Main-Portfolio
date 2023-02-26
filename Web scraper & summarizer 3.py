import requests
from bs4 import BeautifulSoup
import pandas as pd

from newspaper import Config
from newspaper import Article
import nltk


#specifying user agent

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'

config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 10


#specifying url and invoking newspaper3k methods

base_url = 'https://www.reuters.com/world/africa/zimbabwe-compensate-white-former-farmers-over-10-years-instead-20-finmin-2023-02-23/'
article = Article(base_url, config=config)
article.download()
article.parse()
article.nlp()
print(article.summary)


#Creating excell sheet

from openpyxl import Workbook

workbook = Workbook()

worksheet= workbook.active


#titling excell sheet columns

worksheet["a1"] = "Title"
worksheet["a2"] = article.title
worksheet["b1"] ="Summary"
worksheet["b2"] =article.summary
worksheet["c1"]="Source"
worksheet["c2"] = base_url


#wrapping text for better readability

for row in ws.iter_rows():
    for cell in row:
        cell.alignment =  cell.alignment.copy(wrapText=True)

# Saving the new excell file in the apprpriate folder

folder_path = ("C:\\Users\\User\\Documents\\test folder\\")
workbook.save(folder_path + "Testfile.xlsx")

