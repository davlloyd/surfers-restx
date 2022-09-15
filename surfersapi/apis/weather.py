from flask import Blueprint
from flask_restx import Namespace, Resource, fields
from flask import current_app as app
from surfersapi.services import feeds
from surfersapi.services.bom import observations

ns = Namespace("weather", description="Weather forecast information")


"""
Current weather query response object and example
"""

observation = ns.model('observations', {
    'temp': fields.Integer(required=True, description='Current temperature in celcius'),
    'wind_speed': fields.Integer(required=True, description='current wind speed in kmh'),
    'wind_direction': fields.String(required=True, description='Wind direction'),
    'rain_today': fields.Integer(required=True, description='Rain since this morning'),
    'humidity': fields.Integer(required=True, description='Current humidity level'),
})

observation_example = [
    {
        'temp': 23,
        'wind_speed': 10,
        'wind_direction': 'NW',
        'rain_today': 0,
        'humidity': 63,
    }
]

"""
Weather and surf alert return object response layout and example
"""

alert = ns.model('alert', {
    'title': fields.String(required=True, description='Weather alert area'),
    'location': fields.String(required=True, description='Location of the alert'),
    'published': fields.String(required=True, description='Weather alert time'),
    'link': fields.String(required=True, description='Weather alert details location'),
})


alert_example = [
    {
        'title': 'Heavy wind alert NSW',
        'location': 'New South Wales',
        'published': 'some time details',
        'link': 'http://somewhere.weather.com'
    },
]


@ns.route('/observation/<location>')
@ns.param('location', 'The location identifier')
@ns.response(404, 'Location not found')
class observation(Resource):
    @ns.doc('get_observation')
    @ns.marshal_with(observation)
    def get(self, location):
        if location:
            _observations = observations(location)
            '''Get current observed weather from location identifier'''
            return _observations
        else:
            ns.abort(404)


@ns.route('/alert')
class alert(Resource):
    @ns.doc('get_alert')
    @ns.marshal_with(alert)
    def get(self):
        _alert = feeds.getWeather()
        '''Get weather alerts'''
        return _alert
