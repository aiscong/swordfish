from http_caller import *
from instrument import *
from enum import Enum


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

    caller = HttpCaller()

    def __init__(self, username, password):
        self.log_in(username, password)

    def get_positions(self):
        return self.caller.session_get(self.positions_url)

    def get_account(self):
        return self.caller.session_get(self.account_url)['results'][0]

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
        if isinstance(order_type, OrderType):
            raise(ValueError('Invalid order type'))

        payload = {
            'account': self.get_account()['url'],
            'instrument': get_instrument(symbol)['url'],
            'type': OrderType(order_type).value,
            'time_in_type': TimeInForce(time_in_force).value,
            'trigger': Trigger(trigger).value,
            'price': price,
            'stop_price': stop_price,
            'quantity': quantity,
            'side': Side(side).value
        }
        print(payload)

        self.caller.session_post(self.order_url, payload)

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
