import requests

user_data = {'username': 'admin', 'password': '123'}
l = requests.post("http://127.0.0.1:5000/login", data=user_data)
r = requests.post("http://127.0.0.1:5000/register", data=user_data)

print('Print '+l.text)
print('Print '+r.text)

