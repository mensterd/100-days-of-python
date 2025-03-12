import requests
# Import secrets.py that holds api key
import secrets

# API Documentation: https://newsapi.org/docs

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Get the newsapi-key from the secrets module as NEWS_API_KEY
API_KEY = secrets.NEWS_API_KEY

class NewsHead:
    """ Takes <company_name> to search for news for as String and <number_of_articles> to look for """
    def __init__(self, company_name:str, number_of_articles:int=3):
        self.number_of_articles = number_of_articles
        self.news = {}
        self.company_name = company_name
        self.API_KEY = API_KEY
        self.__get_news()


    def __get_news(self):
        """ private method. Do not use outside class """
        params = {
            "qInTitle": self.company_name,
            "language": "en",
            "sortedBy": "publishedAt", # newest articles
            "apiKey": API_KEY,
        }
        response = requests.get(NEWS_ENDPOINT, params=params)
        response.raise_for_status()
        self.news = response.json()


    def get_news(self)->list:
        """ Returns a List of formatted Strings to be sent to user """
        # Get the first <number_of_articles> from the Dictionary and store as List
        news_items = self.news["articles"][:self.number_of_articles]
        # Create a List of formatted Strings per message to send to user
        message_list = [f"{i["title"]}\n{i["url"]}\n" for i in news_items]
        return message_list



if __name__ == "__main__":
    newshead = NewsHead(company_name="Tesla Inc")
    news_list = newshead.get_news()
    print(news_list[0])





