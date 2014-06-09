import requests
import json

query_params = {'access_token': 'API_KEY',
                'longUrl': 'http://picsmashup.com'}

endpoint = 'https://api-ssl.bitly.com/v3/shorten'
response = requests.get(endpoint, params = query_params, verify=False)

data = json.loads(response.content)
print data["data"]["url"]

	
