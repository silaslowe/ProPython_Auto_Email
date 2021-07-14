# 0f56286be30b49f385e348b38d2c9fe3
import requests
from pprint import pprint


class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass


url = 'https://newsapi.org/v2/everything?' \
      'q=nasa&' \
      'from=2021-07-12&' \
      'to=2021-07-14' \
      '&Language=en&' \
      'apiKey=0f56286be30b49f385e348b38d2c9fe3'

response = requests.get(url)
content = response.json()
articles = content['articles']

forEmails = {}

email_body = ''

for article in articles:
    email_body = f"{email_body} \n {article['title']}  \n {article['url']} \n \n"

print(email_body)