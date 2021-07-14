# 0f56286be30b49f385e348b38d2c9fe3
import requests


class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass


response = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=0f56286be30b49f385e348b38d2c9fe3')
content = response.text
print(content)
