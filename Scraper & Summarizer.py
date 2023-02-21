# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, a
from newspaper import Article

#creating our article summary class

def summarize_article(url):
    article = Article(url)
    article.download()
    article.parse()
    article.authors()
    article.summary()
    # a series of print functions to designate the proper format for the data sourced above.
    print(article.authors)
    print(article.summary)



summarize_article("https://www.news24.com/fin24/economy/big-eskom-move-needed-in-the-budget-even-r200bn-in-debt-relief-not-enough-warns-investor-20230221")