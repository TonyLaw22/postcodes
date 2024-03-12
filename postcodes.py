import json
import requests

headers = {'Content-Type': 'application/json'}
json_data = json.dumps({'postcodes': ["OX49 5NU"]})

post_code_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_data)

print(post_code_req.json()['result'][0]['result']['region'])