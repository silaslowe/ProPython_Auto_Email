import time

import yagmail
import pandas
import datetime
from news import NewsFeed

while True:
    now = datetime.datetime.now()
    if now.hour == 20 and now.minute == 23:
        df = pandas.read_excel('silaspeopledun.xlsx')

        for index, row in df.iterrows():
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

            news_feed = NewsFeed(row['interest'], today, yesterday, 'en')
            email = yagmail.SMTP(user="silaslowe1@gmail.com", password="This!sat3st")
            email.send(to=row['email'],
                       subject=f"Your {row['interest']} news for today",
                       contents=f"Hi {row['name']}. \n\n This is Silas. See What's on about {row['interest']}. "
                                f"{news_feed.get()} \n\n-Silas",
                       attachments="design.txt")

    time.sleep(60)
