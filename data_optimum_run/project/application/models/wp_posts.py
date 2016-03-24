# coding: utf-8
import datetime
from ._base import db


class WpPosts(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(200))
    slug = db.Column(db.String(200))
    term_group = db.Column(db.Integer)
    times = db.Column(db.DateTime)

    def __init__(self, name, slug, term_group,times):
        self.name = name
        self.slug = slug
        self.term_group = term_group
        self.times = times

    def __repr__(self):
        return '<Terms %r>' % self.name
