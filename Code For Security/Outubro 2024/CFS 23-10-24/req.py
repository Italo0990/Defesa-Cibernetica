"""REQUESTS"""

import requests
import json

'''
www.url.com/var=valor&
GET
POST
PUT
DELETE
'''

resposta = requests.get('http://ip-api.com/json/24.48.0.1')
# print(resposta.status_code)
# print(resposta.text)
# print(resposta.content)

# resp_json = json.loads(resposta.text)
resp_json = resposta.json()
print(resp_json['city'])