import sys
from flask import Flask
from surfersreport import config
from flask_restx import Api

app = Flask(__name__)

def create_app(config_name):
    app.config.from_object(config.config[config_name])
    config.config[config_name].init_app(app)

    app.logger.info('Import blueprints')
    from surfersreport.apis import blueprint as api
    app.register_blueprint(api, url_prefix='/api/v1')

    return app

