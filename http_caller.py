import requests

class HttpCaller:

    def get(self, url, params={}):
        response = requests.get(url, params=params)
        return response.json()

    def post(self, url, json_payload):
        response = requests.post(url, json=json_payload)
        return response.json
