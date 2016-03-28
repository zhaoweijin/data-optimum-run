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

    # def __repr__(self):
    #     return '<Record %r>' % self.comments

class WpDataoptimumPlay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    desc = db.Column(db.Text)
    operate_time = db.Column(db.DateTime)
    add_time = db.Column(db.DateTime)

class WpDataoptimumPlayContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    from_user = db.Column(db.String(255))
    to_user = db.Column(db.String(255))
    self_symbol = db.Column(db.String(17))
    object_symbol = db.Column(db.String(17))
    content = db.Column(db.Text)
    images = db.Column(db.String(255))
    play_id = db.Column(db.Integer)
    carry_time = db.Column(db.DateTime)
    status = db.Column(db.SmallInteger)