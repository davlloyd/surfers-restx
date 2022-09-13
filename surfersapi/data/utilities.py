import json
import sys
from unicodedata import category
from surfersapi import app
from . import models


class DataManager():

    @staticmethod
    def importData():
        with open(app.config['DATA_FILE'], 'r') as f:
            app.logger.info('Importing data')
            table = json.loads(f.read())
            for _feed in table['feed']:
                models.Feed(name=_feed['name'],
                            location=_feed['location'],
                            category=_feed['category'],
                            url=_feed['url']).add()
                
