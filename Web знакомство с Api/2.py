import requests
import json
from api import apikey

city_list = ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']
coords = []

for city in city_list:
    url = f'https://geocode-maps.yandex.ru/1.x/?apikey={apikey}&format=json&geocode={city}'
    response = requests.get(url).text
    data = json.loads(response)
    coords.append(data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"])

print(coords)