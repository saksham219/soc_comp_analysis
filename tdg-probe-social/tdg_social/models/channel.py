# -*- coding: utf-8 -*-
from tdg_social import db
from tdg_social.models.base import Base


class Channel(Base):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, index=True)
    page_id = db.Column(db.String(40), index=True, unique = True)
    page_name = db.Column(db.String(50), index=True)
    followers = db.Column(db.Integer)
    following = db.Column(db.Integer)
    description = db.Column(db.Text)
    website = db.Column(db.String(50))
    phone = db.Column(db.String(30))
    admin = db.Column(db.Boolean, default=False)
    influencer = db.Column(db.Boolean, default=False, index=True)

    def __init__(self, type, page_id, page_name, followers, following, description, website, phone, admin, influencer):
        self.type = type
        self.page_id = page_id
        self.page_name = page_name
        self.followers = followers
        self.following = following
        self.description = description
        self.website = website
        self.phone = phone
        self.admin = admin
        self.influencer = influencer

    def __repr__(self):
        return '<%s %s %s %s %s %s %s %s %s %s %s>' % (self.id, self.type, self.page_id, self.page_name, self.followers,
                                                    self.following, self.description, self.website, self.phone, self.admin,
                                                 self.influencer)
