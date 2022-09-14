import json
import sys
from unicodedata import category
from flask import jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.inspection import inspect
from surfersapi import app, db
from .utilities import DataManager

app.logger.info('Define DB Models')


class Feed(db.Model):
    __tablename__ = 'feed'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    category = db.Column(db.String(64), unique=False, index=True)
    location = db.Column(db.String(64), unique=False, index=True)
    url = db.Column(db.Text)

    def __repr__(self):
        return self.id

    def add(self):
        _id = None
        db.session.add(self)
        try:
            db.session.commit()
            app.logger.info('Feed Record Added: %s', self.name)
        except IntegrityError:
            db.session.rollback()

        if self.id is None:
            _resp = Feed.query.with_entities(Feed.id).filter(Feed.name == self.name).first()
            _id = _resp["id"]
        else:
            _id = self.id

        return _id

    @staticmethod
    def get():
        result = db.session.query(Feed).all()
        return result


app.logger.info('DB URI: %s',app.config['SQLALCHEMY_DATABASE_URI'])
app.logger.info('Create DB')
with app.app_context():
    db.create_all()
    db.session.commit()
    DataManager.importData()




