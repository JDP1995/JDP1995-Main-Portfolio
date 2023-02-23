# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, a

import requests
from bs4 import BeautifulSoup
import pandas as pd

from newspaper import Config
from newspaper import Article
import nltk


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'

config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 10

nltk.download('punkt')

base_url = 'https://www.reuters.com/world/africa/zimbabwe-compensate-white-former-farmers-over-10-years-instead-20-finmin-2023-02-23/'
article = Article(base_url, config=config)
article.download()
article.parse()
article.nlp()
print(article.summary)













