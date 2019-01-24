from http_caller import *
from instrument import *
from enum import Enum
from quote import *


class Side(Enum):
    BUY = 'buy'
    SELL = 'sell'


class OrderType(Enum):
    MARKET = 'market'
    LIMIT = 'limit'


class Trigger(Enum):
    IMMEDIATE = 'immediate'
    STOP = 'stop'


class TimeInForce(Enum):
    GOOD_FOR_DAY = 'gfd'
    GOOD_TIL_CANCELED = 'gtc'


class Trader:
    auth_token = None
    refresh_token = None
    client_id = 'c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS'
    log_in_url = 'https://api.robinhood.com/oauth2/token/'
    log_out_url = 'https://api.robinhood.com/oauth2/revoke_token/'
    positions_url = 'https://api.robinhood.com/positions/'
    account_url = 'https://api.robinhood.com/accounts/'
    order_url = 'https://api.robinhood.com/orders/'
    get_order_url = 'https://api.robinhood.com/orders/{id}/'

    caller = HttpCaller()

    def __init__(self, username, password):
        self.log_in(username, password)

    def get_positions(self):
        return self.caller.session_get(self.positions_url)

    def get_account(self):
        return self.caller.session_get(self.account_url)['results'][0]

    def market_buy(self, symbol, quantity):
        price = current_quote(self, [symbol]).get(symbol).bid_price
        return self.submit_order(symbol=symbol,
                                 order_type=OrderType.MARKET,
                                 time_in_force=TimeInForce.GOOD_FOR_DAY,
                                 trigger=Trigger.IMMEDIATE,
                                 price=price,
                                 quantity=quantity,
                                 side=Side.BUY)

    def market_sell(self, symbol, quantity):
        price = current_quote(self, [symbol]).get(symbol).bid_price
        return self.submit_order(symbol=symbol,
                                 order_type=OrderType.MARKET,
                                 time_in_force=TimeInForce.GOOD_FOR_DAY,
                                 trigger=Trigger.IMMEDIATE,
                                 price=price,
                                 quantity=quantity,
                                 side=Side.SELL)

    def limit_buy(self, symbol, limit_price, quantity):
        return self.submit_order(symbol=symbol,
                                 order_type=OrderType.LIMIT,
                                 time_in_force=TimeInForce.GOOD_FOR_DAY,
                                 trigger=Trigger.IMMEDIATE,
                                 price=limit_price,
                                 quantity=quantity,
                                 side=Side.BUY)

    def limit_sell(self, symbol, limit_price, quantity):
        return self.submit_order(symbol=symbol,
                                 order_type=OrderType.LIMIT,
                                 time_in_force=TimeInForce.GOOD_FOR_DAY,
                                 trigger=Trigger.IMMEDIATE,
                                 price=limit_price,
                                 quantity=quantity,
                                 side=Side.SELL)

    def stop_market_buy(self, symbol, stop_price, quantity):
        return self.submit_order(symbol=symbol,
                                 order_type=OrderType.MARKET,
                                 time_in_force=TimeInForce.GOOD_FOR_DAY,
                                 trigger=Trigger.STOP,
                                 stop_price=stop_price,
                                 quantity=quantity,
                                 side=Side.BUY)

    def stop_market_sell(self, symbol, stop_price, quantity):
        return self.submit_order(symbol=symbol,
                                 order_type=OrderType.MARKET,
                                 time_in_force=TimeInForce.GOOD_FOR_DAY,
                                 trigger=Trigger.STOP,
                                 stop_price=stop_price,
                                 quantity=quantity,
                                 side=Side.SELL)

    def stop_limit_buy(self, symbol, stop_price, quantity):
        return self.submit_order(symbol=symbol,
                                 order_type=OrderType.LIMIT,
                                 time_in_force=TimeInForce.GOOD_FOR_DAY,
                                 trigger=Trigger.STOP,
                                 stop_price=stop_price,
                                 quantity=quantity,
                                 side=Side.BUY)

    def stop_limit_sell(self, symbol, stop_price, quantity):
        return self.submit_order(symbol=symbol,
                                 order_type=OrderType.LIMIT,
                                 time_in_force=TimeInForce.GOOD_FOR_DAY,
                                 trigger=Trigger.STOP,
                                 stop_price=stop_price,
                                 quantity=quantity,
                                 side=Side.SELL)

    def submit_order(self,
                     symbol='',
                     order_type=None,
                     time_in_force=None,
                     trigger=None,
                     price=None,
                     stop_price=None,
                     quantity=None,
                     side=None):

        symbol = symbol.upper()

        payload = {
            'account': self.get_account()['url'],
            'symbol': symbol,
            'instrument': get_instrument(symbol).url,
            'type': OrderType(order_type).value,
            'time_in_force': TimeInForce(time_in_force).value,
            'trigger': Trigger(trigger).value,
            'price': price,
            'quantity': quantity,
            'side': Side(side).value
        }

        if Trigger(trigger) == Trigger.STOP:
            payload['stop_price'] = stop_price

        print(payload)

        print('======================================')

        order_response = self.caller.session_post(self.order_url, payload)

        print('order id:' + order_response['id'])
        print('order state: ' + order_response['state'])
        return order_response

    def get_order(self, order_id):
        return self.caller.session_get(self.get_order_url.format(id=order_id))

    def cancel_order(self, order):
        return self.caller.session_post(order['cancel'])

    def log_in(self, username, password):
        payload = {'username': username,
                   'password': password,
                   'grant_type': 'password',
                   'client_id': self.client_id}
        log_in_response = self.caller.post(self.log_in_url, payload)

        self.caller.create_session()
        self.caller.set_authorization('Bearer ' + log_in_response['access_token'])
        self.refresh_token = log_in_response['refresh_token']

    def log_out(self):
        payload = {
            'client_id': self.client_id,
            'token': self.refresh_token
        }
        self.caller.session_post(self.log_out_url, payload)

        self.caller.close_session()
        self.auth_token = None
        self.refresh_token = None

    def http_get(self, url, params):
        return self.caller.session_get(url, params)
