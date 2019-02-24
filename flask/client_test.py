import requests

user_data = {'username': 'admin', 'password': '456'}
l = requests.post("http://127.0.0.1:5000/login", data=user_data)
#r = requests.post("http://127.0.0.1:5000/register", data=user_data)
#d = requests.post("http://127.0.0.1:5000/unregister", data=user_data)
#u = requests.post("http://127.0.0.1:5000/update", data=user_data)

print(l.text)
#print(r.text)
#print(d.text)
#print(u.text)

