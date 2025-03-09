from itertools import islice
import requests
import secrets

class StockBrain:
    def __init__(self, stock_symbol:str, nr_days=2):
        """ Takes a <stock_symbol> e.g. 'TSLA' as string to fetch Tesla stock values.
            Optional <nr_days> as the number of days to look back for stock values. Default=2
            Offers <closing_values> as a List of Dict k:date v:closing value
        """
        self.nr_trading_days_history = nr_days
        self.stock_symbol = "TSLA"
        self.closing_values = {}
        self.read_configuration()
        self.get_stock_closing_values()



    def read_configuration(self):
        # Define the API endpoint and your API key
        self.api_key = secrets.STOCK_API_KEY
        self.base_url = 'https://www.alphavantage.co/query'



    def get_stock_closing_values(self):
        """ Fetches stock closing data for <stock_symbol> and
            returns a Dict k:date : v:closing value """

            # Define the parameters for the request
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.stock_symbol,
            "interval": "60min",
            "apikey": self.api_key
        }

        # Make the request
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()

        # Check if the request was successful
        if response.status_code == 200:
            # Convert stock data to Dictionary
            stock_data = response.json()
            try:
                if stock_data.get("information"):
                    raise Exception
                # Extract the time series data, this is a Dict with the tradings days dates in it
                trading_days = stock_data.get("Time Series (Daily)")
                # Get the last number of days to analyze and put them in a new Dict
                last_n_days = dict(islice(trading_days.items(), self.nr_trading_days_history))
                print(last_n_days)

                # Get the closing value of these last days and append to Dict:<closing_values> as k:date(str) v:value(str)
                for key, value in last_n_days.items():
                    k = key
                    v = float(value["4. close"])
                    self.closing_values.update({k: v})
            except:
                print("Out of API-calls for today")


def test_call():
    api_key = "I30GCBR9635RY5HQ"
    base_url = 'https://www.alphavantage.co/query'

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "TSLA",
        "interval": "60min",
        "apikey": api_key
    }

    # Make the request
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    r = response.json()
    try:
        if r.get("information"):
            raise Exception
        else:
            raise Exception
    except:
        print("oops")



if __name__ == "__main__":
    # stock_brain = StockBrain("TSLA")
    # print(stock_brain.closing_values)
    # {'Information': 'We have detected your API key as I30GCBR9635RY5HQ and our standard API rate limit is 25 requests per day. Please subscribe to any of the premium plans at https://www.alphavantage.co/premium/ to instantly remove all daily rate limits.'}

    test_call()