import requests

params = {'list_param': ['value1', 'value2']}
url = 'http://static-maps.yandex.ru/1.x/'
headers = {'user-agent': 'yandexlyceum/1.1.1'}
response = requests.get(url, headers=headers, params=params)
print(response.url)
print('222')
