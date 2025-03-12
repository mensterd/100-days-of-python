from telegram_sender import TelegramSender
from stockbrain import StockBrain
from newshead import NewsHead

# JSON File viewer: https://jsonviewer.stack.hu/

# The stock to monitor
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# The margin the stockprice needs to drop or rise before a message is send
STOCK_MARGIN = 1.0





def send_message(message:str)->bool:
    """ Sends a message with Telegram messenger. Takes string returns bool. """
    telegram = TelegramSender()
    result = telegram.send_message(message)
    return result


def get_separator_message(stockbrain:StockBrain)->str:
    """ Creates the separator line. Takes Stockbrain object as input, returns String """
    # If positive percentage, stockprice is rising, else stockprice is falling.
    if stockbrain.stock_drop:
        up_down = "🔻"
    else:
        up_down = "🔺"

    result = f"{stockbrain.stock_symbol} {up_down} {stockbrain.stock_change_percentage}\n"
    return result


def main():
    # Create stockbrain object
    stockbrain = StockBrain(STOCK)
    # Get the dictionary k:date(str) : v:value(float)
    if stockbrain.stock_change_percentage > STOCK_MARGIN:
        # Create newshead object
        newshead = NewsHead(company_name=COMPANY_NAME, number_of_articles=3)
        # get the news as List of formatted Strings from newshead
        message_list = newshead.get_news()

        for m in message_list:
            message = f"{get_separator_message(stockbrain)}{m}"
            send_message(message)

    else:
        # Stockprice change is within margin
        print(f"Stockprice within {STOCK_MARGIN}% margin: {stockbrain.stock_change_percentage}%")


if __name__ == "__main__":
   main()