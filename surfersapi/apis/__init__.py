from flask import Blueprint
from flask_restx import Resource, Api
from .weather import ns as weather_ns
from .surf import ns as surf_ns
from .general import ns as general_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    version="1.0",
    title="Weather and Surf Forecast REST API",
    description="A REST API for swell and weather coditions",
)

api.add_namespace(weather_ns)
api.add_namespace(surf_ns)
api.add_namespace(general_ns, path='/')
