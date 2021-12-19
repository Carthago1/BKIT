import requests
from config import appid

def weather_forecast(*args):
    try:
        if len(args) == 3:
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                        params={'lon': args[0], 'lat': args[1],  'units': 'metric',
                        'lang': 'ru', 'APPID': appid})
            day = args[2]
            
        else:
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                    params={'q' : args[0],  'units': 'metric','lang': 'ru', 'APPID': appid})
            day = args[1]
        
        data = res.json()    
        i = 0
        for f in data['list']:
            if i == day:
                return f
            i += 1 
    except Exception as e:
        print("Exception:", e)
