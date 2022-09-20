import sys
from flask import Flask
from surfersapi import config
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from surfersapi.data.utilities import DataManager


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.config[config_name])
    config.config[config_name].init_app(app)

    with app.app_context():
        app.logger.info('Setup Data Models')
        from surfersapi.data.models import db
        db.init_app(app)
        DataManager.initDB()
    
        app.logger.info('Import blueprints')
        from surfersapi.apis import blueprint as api
        app.register_blueprint(api, url_prefix='/api/v1')

    return app

