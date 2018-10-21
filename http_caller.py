import urllib.request
import json


class HttpCaller:
    def get(self, url):
        response = urllib.request.urlopen(url)
        return json.load(response)
