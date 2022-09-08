from flask import Blueprint
from flask_restx import Namespace, Resource, fields
from flask import current_app as app

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


@ns.route('/swell/<int:location_id>')
@ns.param('location_id', 'The location identifier')
@ns.response(404, 'Location not found')
class swell(Resource):
    @ns.doc('get_swell')
    @ns.marshal_with(swell)
    def get(self, location_id):
        if location_id > 0:
            '''Get swell forecast from location identifier'''
            return swell_example
        else:
            ns.abort(404)



@ns.route('/water/<int:location_id>')
@ns.param('location_id', 'The location identifier')
@ns.response(404, 'Location not found')
class water(Resource):
    @ns.doc('get_water')
    @ns.marshal_with(water)
    def get(self, location_id):
        if location_id > 0:
            '''Get water forecast from location identifier'''
            return water_example
        else:
            ns.abort(404)



