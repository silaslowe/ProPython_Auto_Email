import yagmail
import pandas
from news import NewsFeed

df = pandas.read_excel('silaspeopledun.xlsx')

for index, row in df.iterrows():
    news_feed = NewsFeed(row['interest'], '2021-07-13', '2021-07-14', 'en')
    email = yagmail.SMTP(user="silaslowe1@gmail.com", password="This!sat3st")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today",
               contents=f"Hi {row['name']}. \n\n This is Silas. See What's on about {row['interest']}. "
                        f"{news_feed.get()} \n\n-Silas",
               attachments="design.txt")

