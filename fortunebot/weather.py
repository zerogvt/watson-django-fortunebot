import requests
from . import config

def process(arg):
    countrycode = arg.replace(config.WEATHER_TRIGGER,'').strip()
    api = config.WEATHER_URL + "/v1/country/{1}/alerts.json".format(countrycode)
    res = requests.get(api, timeout=5)
    return res
