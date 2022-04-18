""" Python project to read public data returned from URL, and parsing JSON to a
dictionary object. """

from urllib.request import urlopen
import json
def public_data (url):
    try:
        response = urlopen(url)
        data_json = json.loads(response.read())
        data_dict = dict(data_json)
    except:
        raise ConnectionError ("Response cannot be retrieved")
    return data_dict

# print(public_data("https://api.github.com"))
# print(public_data("https://api.google.com"))