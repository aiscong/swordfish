import requests
from six.moves.urllib.request import getproxies


class HttpCaller:
    session = None

    @staticmethod
    def get(url, params={}):
        response = requests.get(url, params=params)
        return response.json()

    @staticmethod
    def post(url, json_payload):
        response = requests.post(url, json=json_payload)
        return response.json()

    def session_get(self, url, params={}):
        response = self.session.get(url, params=params)
        return response.json()

    def session_post(self, url, json_payload):
        response = self.session.post(url, json=json_payload)
        return response.json()

    def create_session(self):
        self.session = requests.session()
        self.session.proxies = getproxies()
        self.session.headers = {'Connection': 'keep-alive'}

    def set_authorization(self, auth_token):
        self.session.headers['Authorization'] = auth_token

    def close_session(self):
        self.session.close()
