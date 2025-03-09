from telegram_sender import TelegramSender
from stockbrain import StockBrain
from newshead import NewsHead
from datetime import datetime
import requests


# JSON File viewer: https://jsonviewer.stack.hu/


STOCK = "TSLA"
STOCK_MARGIN = 5.0
COMPANY_NAME = "Tesla Inc"


# STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



def calculate_difference(values:tuple)->float:
    """ Takes Tuple of two floats. Returns positive or negative percentage as float"""
    difference = values[0] - values[1]
    percentage = (difference / values[1]) * 100
    return round(percentage, 2)



def send_message(message:str)->bool:
    telegram = TelegramSender()
    result = telegram.send_message(message)
    return result



def convert_date(str_date:str)->datetime:
    """ Takes string formatted date, returns datetime object. Requires datetime import. """
    # Set input format mask
    date_format = "%Y-%m-%d"
    # format date string to datetime object and return value
    dt = datetime.strptime(str_date, date_format)
    return dt


def get_separator_message(percentage:float, stock:str)->str:
    if percentage >= 0:
        result = f"\n{stock} 🔺{percentage}\n"
    else:
        result = f"\n{stock} 🔻{percentage}\n"
    return result


def main():
    stockbrain = StockBrain(STOCK)
    # Get the dictionary k:date(str) : v:value(float)
    closing_values_dict = stockbrain.closing_values
    print(closing_values_dict)
    # Get only the values  from the Dict and store in a List.
    closing_values = list(closing_values_dict.items())
    print(closing_values)

    start_date = closing_values[0][0]
    end_date = closing_values[-1][0]

    closing_value_day_1 = closing_values[0][1]
    closing_value_day_2 = closing_values[-1][1]


    percentage = calculate_difference((closing_value_day_1, closing_value_day_2))
    if percentage < -STOCK_MARGIN or percentage > STOCK_MARGIN:
        newshead = NewsHead(company_name=COMPANY_NAME, from_date=start_date, to_date=end_date, num_articles=2)
        news_list = newshead.get_news()

        # # Call function to create a separator message and join this string with the news-messages
        text_message = get_separator_message(percentage, STOCK)
        text_message += get_separator_message(percentage, STOCK).join(news_list)
        print(text_message)
        send_message(text_message)

    else:
        print(f"Within {STOCK_MARGIN}%: {percentage}")


if __name__ == "__main__":
   main()