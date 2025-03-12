import requests




class StockBrain:
    def __init__(self, stock_symbol:str):
        """ Takes a <stock_symbol> e.g. 'TSLA' as string to fetch Tesla stock values.
            Optional <nr_days> as the number of days to look back for stock values. Default=2
            Offers <closing_values> as a List of Dict k:date v:closing value
        """
        self.stock_symbol = stock_symbol
        self.daily_difference = float
        self.trading_days_list = []
        self.stock_drop = bool
        self.stock_change_percentage = 0.0
        self.__read_configuration()
        self.__get_stock_closing_values()
        self.__calculate_percentage()


    def __read_configuration(self):
        # Define the API endpoint and your API key
        self.api_key = "I30GCBR9635RY5HQ"
        self.base_url = 'https://www.alphavantage.co/query'



    def __get_stock_closing_values(self):
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
            # Convert stock data to json format
            stock_data = response.json()
            try:
                # If the key "information" exists in the result, then the max nr of daily api-calls was achieved
                if stock_data.get("information"):
                    print(stock_data.get("information"))
                    raise Exception
                # Extract the time series data, this is a Dict with the tradings days dates in it
                trading_days = stock_data.get("Time Series (Daily)")
                # Make a list of only the values of trading_days Dictionary
                self.trading_days_list = [v for (k, v) in trading_days.items()]

            except Exception as e:
                print(f"Out of daily API-calls {e}")


    def __calculate_percentage(self):
        # Get the closing stockprices of yesterday and the day before
        yesterday = self.trading_days_list[0]["4. close"]
        day_before_yesterday = self.trading_days_list[1]["4. close"]

        # Calculate the difference and the percentage
        difference = float(yesterday) - float(day_before_yesterday)
        self.stock_change_percentage = difference / float(day_before_yesterday) * 100
        # If the difference is negative, a price drop, set Drop to True and make percentage positive
        if difference < 0:
            self.stock_drop = True
            self.stock_change_percentage *= -1
        else:
            self.stock_drop = False




if __name__ == "__main__":
    stock_brain = StockBrain("TSLA")
