# ef66f0f902c4f18bad522899e2b7c2b6
import requests
from datetime import datetime

url_history = 'https://api.openweathermap.org/data/2.5/onecall'
lat = '57.90'
lon = '59.98'
exclude = 'daily.sunrise'
units = 'metric'
appid = 'ef66f0f902c4f18bad522899e2b7c2b6'
lang = 'ru'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

params = {'lat': lat,
          'lon': lon,
          'exclude': exclude,
          'units': units,
          'appid': appid,
          'lang': lang}
response = requests.get(url_history, params=params, headers=headers)
j_data = response.json()

day_durations = []

for i in range(5):
    a = (j_data['daily'][i]['sunset'] - j_data['daily'][i]['sunrise'])
    hours = (a // 3600)
    minute = ((a - a // 3600 * 3600) // 60)
    sec = a - 3600 * hours - minute * 60
    day_duration = str(hours) + ':' + str(minute) + ':' + str(sec)
    day = datetime.fromtimestamp(j_data['daily'][i]['sunset']).strftime('%Y-%m-%d')
    day_durations.append([a, day_duration, day])

print(day_durations[day_durations.index(max(day_durations))][1], '- максимальная продолжительность светового дня',
      day_durations[day_durations.index(max(day_durations))][2])
