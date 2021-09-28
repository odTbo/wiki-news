from scrapers.constants import *
from requests_html import HTMLSession


class ReutersScraper:
    NAME = "REUTERS"

    def __init__(self):
        self.session = HTMLSession()

    # def get_article_body(self, link):
    #     """Scrapes article's body from it's page."""
    #
    #     # Article page text
    #     r = self.session.get(link, headers=headers)
    #
    #     # Article's paragraphs
    #     paragraphs = r.html.find("#clanok > p")
    #
    #     # Text from all paragraph's separated with 2 line breaks
    #     article_text = "<br><br>".join(p.text for p in paragraphs if len(p.text) != 0)
    #
    #     return article_text

    def get_articles(self) -> list:
        """Scrapes top articles in the past 24h."""

        print("Fetching Reuters...")
        r = self.session.get(url=reuters_url, headers=headers, params=reuters_query)
        r.raise_for_status()

        articles = r.json()["result"]["articles"]
        print("Number of articles: {}".format(len(articles)))

        for article in articles:
            print(article["title"])
            print(article["description"])

        # # GET ARTICLES
        # print("Compiling articles...")
        # for item in item_list:
        #     title = item.text
        #     link = item.attrs["href"]
        #     body = self.get_article_body(link)
        #
        #     articles.append({
        #         "title": title,
        #         "body": body
        #     })
        #
        # print(f"Number of articles: {len(articles)}")
        return articles


if __name__ == "__main__":
    s = ReutersScraper()
    print(s.get_articles())
