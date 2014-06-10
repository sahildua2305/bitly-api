import requests
import json

query_params = {'access_token': 'API_KEY',
		'link': 'http://bit.ly/1oEEBJh'}

endpoint = "https://api-ssl.bitly.com/v3/link/clicks"
response = requests.get(endpoint, params = query_params, verify=False)

data = json.loads(response.content)
print data["data"]["link_clicks"]
