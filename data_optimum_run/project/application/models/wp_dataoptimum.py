# coding: utf-8
import datetime
from ._base import db


class WpDataoptimumRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    config_id = db.Column(db.SmallInteger)
    url = db.Column(db.String(150))
    comments = db.Column(db.String(255))
    user_login = db.Column(db.String(60))
    category = db.Column(db.String(100))
    times = db.Column(db.Integer)
    state = db.Column(db.SmallInteger)

    def __repr__(self):
        return '<Record %r>' % self.comments
