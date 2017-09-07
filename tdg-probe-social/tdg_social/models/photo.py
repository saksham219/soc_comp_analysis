# -*- coding: utf-8 -*-
from tdg_social import db
from tdg_social.models.base import Base


class Photo(Base):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String(40), db.ForeignKey('post.post_id'),index=True)
    photo_desc = db.Column(db.Text)
    photo = db.Column(db.String(900), index=True)

    def __init__(self, post_id, photo_desc, photo):
        self.post_id = post_id
        self.photo_Desc = photo_desc
        self.photo = photo

    def __repr__(self):
        return '<%s %s %s>' %(self.post_id, self.photo_desc, self.photo)
