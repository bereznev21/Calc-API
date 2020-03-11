import requests

host = 'http://localhost:8080'

a = {'expression': 'a+b*10-c*d'" \
               ", 'variables': {'a': 10, 'b': 12, 'c': 23, 'd': 30}}
response = requests.post(host, json=a)
b = response.json()
response1 = requests.get(host, json=b)
print(response1.text)
