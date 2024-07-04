# Api Key: eef7a28b50a14c5f96a25deece34f96a
import requests


class NewsFeed:
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "eef7a28b50a14c5f96a25deece34f96a"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()
        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content["articles"]
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


if __name__ == "__main__":
    news_feed = NewsFeed("nasa", "2024-06-27", "2024-06-28", "en")
    print(news_feed.get())