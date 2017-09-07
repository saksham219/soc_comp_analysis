# -*- coding: utf-8 -*-
from tdg_social import db
from tdg_social.models.base import Base

class Hash(Base):
    id = db.Column(db.Integer, primary_key=True,index=True)
    hashtag = db.Column(db.String(50),index = True, unique=True)

    def __init__(self,hashtag):
        self.hashtag = hashtag

    def __repr__(self):
        return '<%s %s>' % (self.id,self.hashtag)

association_tags = db.Table('tags',Base.metadata,
    db.Column('tag_id', db.Integer, db.ForeignKey('hash.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)