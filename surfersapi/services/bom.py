from enum import Enum, unique
from flask import current_app as app
from . import web

def observations(location):
    _geohash = _locationgeohash(location)
    if _geohash:
        _observations = web.get(API_URL.OBSERVATIONS.set_location(_geohash))
        _data = {
            'temp': _observations['data']['temp'],
            'wind_speed': _observations['data']['wind']['speed_kilometre'],
            'wind_direction': _observations['data']['wind']['direction'],
            'rain_today': _observations['data']['rain_since_9am'],
            'humidity': _observations['data']['humidity']
        }
        return _data
    else:
        return None


def _locationgeohash(location):
    _search = location.replace(" ", "+").replace("_", "+").replace(",", "+")
    _location = web.get(API_URL.LOCATION_SEARCH.set_location(_search))
    if len(_location['data']) > 0:
        _geohash = _location['data'][0]['geohash'][:6]
        return _geohash
    else:
        return None


@unique
class API_URL(Enum):
    LOCATION_SEARCH = 'https://api.weather.bom.gov.au/v1/locations?search={}'
    OBSERVATIONS = 'https://api.weather.bom.gov.au/v1/locations/{}/observations'
    FORECAST_DAILY = 'https://api.weather.bom.gov.au/v1/locations/{}/forecasts/daily'
    FORECAST_3HRLY = 'https://api.weather.bom.gov.au/v1/locations/{}/forecasts/3-hourly'

    def set_location(self, location):
        _url = self.value.format(location)
        return _url
