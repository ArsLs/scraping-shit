import requests
from json import loads
from urllib3 import disable_warnings
from pyuseragents import random as random_useragent

disable_warnings()
token = ''
with open('token.txt') as f:
    token = f.readline()

sesh = requests.Session()
sesh.headers.update({'user-agent': random_useragent(), 'Content-Type': 'application/json', 'X-Wix-Client-Artifact-Id': 'wix-form-builder'})
# session.headers['authorization'] = token
r = sesh.get('https://opensea.io/collection/car-tooned', verify=False)
# if 'username' not in loads(r.text):
#     raise Exception('invalidtoken')
print(r.text)
