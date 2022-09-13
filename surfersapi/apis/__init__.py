from flask import Blueprint
from flask_restx import Resource, Api
from .forecast import ns as forecast_ns
blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    version="1.0",
    title="Swell Forecast REST API",
    description="A REST API for swell and weather coditions",
)

api.add_namespace(forecast_ns)
