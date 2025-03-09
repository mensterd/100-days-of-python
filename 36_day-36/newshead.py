import requests
import secrets

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK = "TSLA"
# STOCK_MARGIN = 2.0
COMPANY_NAME = "Tesla Inc"

API_KEY = secrets.NEWS_API_KEY

class NewsHead:
    def __init__(self, company_name, from_date, to_date, num_articles=2):
        self.from_date = from_date
        self.to_date = to_date
        self.num_articles = num_articles
        self.news = {}
        self.company_name = company_name
        self.API_KEY = API_KEY
        self.__get_news()


    def __get_news(self):
        params = {
            "q": self.company_name,
            "from": self.from_date,
            "to": self.to_date,
            "language": "en",
            "sortedBy": "relevancy",
            "pageSize": self.num_articles,
            "page": 1,
            "apiKey": API_KEY,
        }
        response = requests.get(NEWS_ENDPOINT, params=params)
        response.raise_for_status()
        self.news = response.json()


    def get_news(self):
        news_items = self.news["articles"][0:self.num_articles]
        news_list = []
        for item in news_items:
            news_list.append(f"{item["title"]}\n{item["description"]}\nRead more: {item["url"]}")

        return news_list





if __name__ == "__main__":

    newshead = NewsHead(company_name=COMPANY_NAME, from_date="2025-03-07", to_date="2025-03-06")
    print(newshead.news)
    nl = newshead.get_news()

    print(nl[0])
    print(nl[1])

        # """
        #     TSLA: 🔺2%
        #     Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
        #     Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
        #     or
        #     "TSLA: 🔻5%
        #     Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
        #     Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
        #     """




