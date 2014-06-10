import requests
import json

query_params = {'access_token': 'API_KEY',
                'link': 'http://bit.ly/byTYvf',
                'unit': 'minute',
                'units': 15}

endpoint = 'https://api-ssl.bitly.com/v3/link/referrers'
response = requests.get(endpoint, params=query_params, verify=False)

data = json.loads(response.content)
print data["data"]["referrers"]
