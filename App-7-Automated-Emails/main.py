import yagmail
import pandas as pd
from news import NewsFeed
import datetime
import time


def send_email():
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday.strftime('%Y-%m-%d'),
                         to_date=today.strftime('%Y-%m-%d'),
                         language='en')
    email = yagmail.SMTP('sooseokkim99@gmail.com', password="ljmwozhcdzxolevv")
    email.send(to=row['email']
               , subject=f"Your {row['interest']} News",
               contents=f"Hi {row['name']} \n See what's on about {row['interest']} today"
                        f"\n {news_feed.get()}"
               )


while True:

    if datetime.datetime.now().hour == 12 and datetime.datetime.now().minute == 0:
        df = pd.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)


