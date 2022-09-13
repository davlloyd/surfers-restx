from flask import Blueprint
from flask_restx import Namespace, Resource, fields
from flask import current_app as app
from surfersapi.services import feeds

ns = Namespace("forecast", description="Forecast operations")

swell = ns.model('swell', {
    'height': fields.Integer(required=True, description='The wave height'),
    'interval': fields.Integer(required=True, description='Interval between waves'),
    'direction': fields.String(required=True, description='Swell source direction'),
})


swell_example = [
    {
        'height': 6,
        'interval': 11,
        'direction': 'SE'
    },
]

water = ns.model('water', {
    'temperature': fields.Integer(required=True, description='The oceans water temperature'),
})


water_example = [
    {'temperature': 22},
]

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


@ns.route('/swell/<location_id>')
@ns.param('location_id', 'The location identifier')
@ns.response(404, 'Location not found')
class swell(Resource):
    @ns.doc('get_swell')
    @ns.marshal_with(swell)
    def get(self, location_id):
        if location_id:
            '''Get swell forecast from location identifier'''
            return swell_example
        else:
            ns.abort(404)



@ns.route('/water/<location_id>')
@ns.param('location_id', 'The location identifier')
@ns.response(404, 'Location not found')
class water(Resource):
    @ns.doc('get_water')
    @ns.marshal_with(water)
    def get(self, location_id):
        if location_id:
            '''Get water forecast from location identifier'''
            return water_example
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
