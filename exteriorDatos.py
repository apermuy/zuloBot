import json
import time
from pyowm import OWM
import configparser

# Create an instance of the ConfigParser class
config = configparser.ConfigParser()  

# Read the contents of the `config.ini` file:
config.read('config.ini')

owm = OWM(config.get('Configuracion', 'OwmKey'))

def obtener(owm_api_key, location):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(location)
    w = observation.weather
    w.wind()                  # {'speed': 4.6, 'deg': 330}
    w.humidity                # 87
    w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    data = json.dumps(w.temperature('celsius'))
    data_json = json.loads(data)
    temp=str(round(data_json["temp"],1))
    tempok=temp.replace(".","-")
    return temp