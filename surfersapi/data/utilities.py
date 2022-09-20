import json
import os
import sys
from unicodedata import category
from flask import current_app as app
from surfersapi.data.models import db, Feed
from . import models


class DataManager():

    @staticmethod
    def initDB():
        app.logger.info('DB URI: %s',app.config['SQLALCHEMY_DATABASE_URI'])
        app.logger.info('Create DB')
        
        _localfile = os.path.join(os.getcwd(), 'data.sqlite')
        if os.path.exists(_localfile):
            os.remove(_localfile)
        db.create_all()
        db.session.commit()
        DataManager.importData()

    @staticmethod
    def importData():
        app.logger.info('Importing data')
        try:
            with open(app.config['DATA_FILE'], 'r') as f:
                table = json.loads(f.read())
        except:
            app.logger.error(f"Error reading data import file: {app.config['DATA_FILE']}")
        else:
            for _feed in table['feed']:
                Feed(name=_feed['name'],
                            location=_feed['location'],
                            category=_feed['category'],
                            url=_feed['url']).add()
            app.logger.info(f"Data import completed")
                
