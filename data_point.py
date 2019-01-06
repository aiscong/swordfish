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

    def __repr__(self):
        return str(self.timestamp.time()) + " -> $" + str(self.price)

class HistoricalPoint:

    def __init__(self, json_response):
        self.timestamp = datetime.datetime.strptime(json_response["begins_at"], DATETIME_FORMAT)
        self.open = float(json_response["open_price"])
        self.close = float(json_response["close_price"])
        self.high = float(json_response["high_price"])
        self.low = float(json_response["low_price"])
        self.vol = int(json_response["volume"])

    def __repr__(self):
        return str(self.timestamp.time()) + " -> $" + str(self.open)

class Instrument:

    def __init__(self, json_response):
        self.id = json_response['id']
        self.symbol = json_response['symbol']

    def __repr__(self):
        return str(self.symbol) + " -> " + str(self.id)