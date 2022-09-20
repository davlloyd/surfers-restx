import json
import sys
from unicodedata import category
from flask import jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.inspection import inspect

db = SQLAlchemy()

class Feed(db.Model):
    __tablename__ = 'feed'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    category = db.Column(db.String(64), unique=False, index=True)
    location = db.Column(db.String(64), unique=False, index=True)
    url = db.Column(db.Text)

    def __init__(self, name: str, category: str, location: str, url: str):
        self.name = name
        self.url = url
        self.location = location
        self.category = category
        self.id = self.add()

    def __repr__(self):
        return self.id

    def add(self):
        _id = None
        db.session.add(self)
        try:
            db.session.commit()
            current_app.logger.info('Feed Record Added: %s', self.name)
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





