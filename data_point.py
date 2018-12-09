import datetime


# Global Variables
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class CurrentPoint:

    def __init__(self, json_response):
        self.ask_price = float(json_response["ask_price"])
        self.ask_size = int(json_response["ask_size"])
        self.bid_price = float(json_response["bid_price"])
        self.bid_size = int(json_response["bid_size"])
        self.price = float(json_response["last_trade_price"])
        self.previous_close_price = float(json_response["adjusted_previous_close"])
        self.previous_close_date = datetime.datetime.strptime(json_response["previous_close_date"], DATE_FORMAT).date()
        self.symbol = json_response["symbol"]
        self.timestamp = datetime.datetime.strptime(json_response["updated_at"], DATETIME_FORMAT)




