#!/usr/bin/env python3

import requests
from pprint import pprint

URL = "http://127.0.0.1:2224/spaceballs-api"

resp = requests.get(URL).json()

# for char in list(resp.keys()):
#     print(char)

pprint(resp)

