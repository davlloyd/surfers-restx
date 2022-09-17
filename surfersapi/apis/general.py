from flask import Blueprint
from flask_restx import Namespace, Resource, fields
from flask import current_app as app

ns = Namespace("general", description="General service relate APIs")

"""
General API services
"""


healthz = ns.model('healthz', {
    'health': fields.String(required=True, description='General service status'),
    'environment': fields.String(required=True, description='Current application environment'),
    'database': fields.String(required=True, description='Current application environment'),
})



# Status query page, can also be used for the benchmark testing 
@ns.route('healthz')
class health(Resource):
    @ns.doc('get_healthz')
    @ns.marshal_with(healthz)
    def get(self):
        _status = {
            "health": "ok",
            "environment": app.config['ENV'],
            "database": app.config['SQLALCHEMY_DATABASE_URI'][:10]
        }
        return _status
