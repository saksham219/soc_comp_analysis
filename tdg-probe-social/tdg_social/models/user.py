# -*- coding: utf-8 -*-
from tdg_social import db
from tdg_social.models.base import Base

class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    user_id  = db.Column(db.String(40), index=True)
    user_name = db.Column(db.String(40))
    user_screen_name = db.Column(db.String(40))
    user_description = db.Column(db.Text)
    user_photo = db.Column(db.Text)
    page_id = db.Column(db.String(50), db.ForeignKey('channel.page_id'),index=True)

    def __init__(self,user_id, user_name,user_screen_name,user_description,user_photo, page_id):
        self.user_id = user_id
        self.user_name = user_name
        self.user_screen_name = user_screen_name
        self.user_description = user_description
        self.user_photo = user_photo
        self.page_id = page_id

    def __repr__(self):
        return '<%s %s %s %s %s %s>' %(self.user_id,self.user_name,self.user_screen_name,self.user_description,
                                 self.user_photo,self.page_id)

