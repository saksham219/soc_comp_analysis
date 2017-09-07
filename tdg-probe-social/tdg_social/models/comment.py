# -*- coding: utf-8 -*-
from tdg_social import db

from tdg_social.models.base import Base


class Comment(Base):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String(40), db.ForeignKey('post.post_id'), index=True)
    user_id = db.Column(db.String(40), index=True)
    user_name = db.Column(db.String(800))
    user_message = db.Column(db.Text)

    def __init__(self, post_id, user_id, user_name, user_message, user_created_time):
        self.post_id = post_id
        self.user_id = user_id
        self.user_name = user_name
        self.user_message = user_message
        self.user_created_time =user_created_time

    def __repr__(self):
        return '<%s %s %s %s %s>' %(self.post_id, self.user_id, self.user_name, self.user_message,
                                          self.user_created_time)

