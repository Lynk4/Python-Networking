import requests

proxies = {
# random ip..........
    'https': 'https://43.134.91.82:3128'
}
response = requests.get("https://ipinfo.io/json", proxies=proxies)

print(response.json()['country'])
print(response.text)
