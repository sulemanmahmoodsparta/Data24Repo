import requests
from pprint import pprint

request_bbc = requests.get("https://www.bbc.co.uk/")


pprint(request_bbc.headers)

