# ef66f0f902c4f18bad522899e2b7c2b6
import requests
from datetime import datetime, timezone, timedelta
import time

min_diff = []
current_date = datetime.now().date()
a = int(time.mktime(current_date.timetuple()))
tz = timezone(+timedelta(hours=5))

url_history = 'https://api.openweathermap.org/data/2.5/onecall/timemachine'
lat = '57.90'
lon = '59.98'
units = 'metric'
appid = 'ef66f0f902c4f18bad522899e2b7c2b6'
lang = 'ru'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

for l in range(4):
    dt = a
    params = {'lat': lat,
              'lon': lon,
              'dt': dt,
              'units': units,
              'appid': appid,
              'lang': lang}

    response = requests.get(url_history, params=params, headers=headers)
    j_data = response.json()
    b = len(j_data['hourly'])
    m = []
    n = []
    k = []
    c = a
    for i in range(4):
        c = c + 3600
        n.append(c)

    for i in range(b):
        for j in range(len(n)):
            if j_data['hourly'][i]['dt'] == n[j]:
                k.append(j_data['hourly'][i])
            else:
                continue

    for i in range(len(k)):
        m.append(k[i]['temp'] - k[i]['feels_like'])
    min_diff.append([min(m), a])
    a = a - 86400

print('Минимальная разница температур', min_diff[min_diff.index(min(min_diff))][0], 'градусов Цельсия')
print('Время', datetime.fromtimestamp(min_diff[min_diff.index(min(min_diff))][1], tz).strftime('%Y-%m-%d %H:%M'))
