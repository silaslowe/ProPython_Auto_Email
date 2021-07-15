# 0f56286be30b49f385e348b38d2c9fe3
import requests
from pprint import pprint


class NewsFeed:
    """Representing news articles form newsapi.org based on users interests"""

    base_url = 'https://newsapi.org/v2/everything?'
    api_key = '0f56286be30b49f385e348b38d2c9fe3'

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f'{self.base_url}' \
              f'q={self.interest}&' \
              f'from={self.from_date}' \
              f'to={self.to_date}' \
              f'&Language={self.language}&' \
              f'apiKey={self.api_key}'

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''

        for article in articles:
            email_body = f"{email_body} \n {article['title']}  \n {article['url']} \n \n"

        return email_body

if __name__ == "__main__":
    newsfeed = NewsFeed('nasa', '2021-07-13', '2021-07-14', 'en')
    print(newsfeed.data)

