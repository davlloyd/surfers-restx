import json
import sys
from unicodedata import category
from surfersapi import app
from . import models


class DataManager():

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
                models.Feed(name=_feed['name'],
                            location=_feed['location'],
                            category=_feed['category'],
                            url=_feed['url']).add()
            app.logger.info(f"Data import completed")
                
