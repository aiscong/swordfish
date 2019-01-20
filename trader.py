from http_caller import *


class Trader:

    auth_token = None
    refresh_token = None
    client_id = 'c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS'
    log_in_url = 'https://api.robinhood.com/oauth2/token/'
    log_out_url = 'https://api.robinhood.com/oauth2/revoke_token/'
    positions_url = 'https://api.robinhood.com/positions/'

    caller = HttpCaller()

    def __init__(self, username, password):
        self.log_in(username, password)

    def get_positions(self):
        return self.caller.session_get(self.positions_url)

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
