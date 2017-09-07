# -*- coding: utf-8 -*-
from tdg_social import db
from tdg_social.models.base import Base


class Like(Base):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String(40), db.ForeignKey('post.post_id'), index=True)
    user_id = db.Column(db.String(40), index=True)
    user_name = db.Column(db.String(200))

    def __init__(self, post_id, user_id, user_name):
        self.post_id = post_id
        self.user_id = user_id
        self.user_name = user_name

    def __repr__(self):
        return '<%s %s %s>' %(self.post_id, self.user_id, self.user_name)
