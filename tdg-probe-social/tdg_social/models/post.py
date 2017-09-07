# -*- coding: utf-8 -*-
from tdg_social import db
from tdg_social.models.base import Base
from tdg_social.models.hash import association_tags
from sqlalchemy.ext.hybrid import hybrid_property

class Post(Base):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String(40), unique=True)
    post_type = db.Column(db.String(10), index=True)
    post_created_time = db.Column(db.DateTime(timezone=True), index=True)
    post_content = db.Column(db.Text)
    post_link = db.Column(db.String(700))
    post_likes = db.Column(db.Integer, index=True)
    post_comments = db.Column(db.Integer, index=True)
    post_shares = db.Column(db.Integer, index=True)
    post_photos = db.Column(db.ARRAY(db.String(500)))
    page_id = db.Column(db.Integer,db.ForeignKey('channel.id'),index=True)
    hashtags = db.relationship('Hash', secondary=association_tags,
                           backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, post_id, post_type, post_created_time, post_content, post_link,
                 post_likes, post_comments, post_shares, post_photos, page_id):
        self.post_id = post_id
        self.post_type = post_type
        self.post_created_time = post_created_time
        self.post_content = post_content
        self.post_link = post_link
        self.post_likes = post_likes
        self.post_comments = post_comments
        self.post_shares = post_shares
        self.post_photos = post_photos
        self.page_id = page_id

    @hybrid_property
    def get_hash(self):
        hashtag_list = list({i.strip("#") for i in self.__getattribute__('post_content').split() if i.startswith("#")})
        return hashtag_list

    def __repr__(self):
        return '<%s %s %s %s %s %s %s %s %s %s >' % (self.post_id, self.post_type, self.post_created_time,self.post_content,
                                                           self.post_link, self.post_likes,self.post_comments, self.post_shares,
                                                           self.post_photos, self.page_id)


class PostInsight(Base):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String(40), db.ForeignKey('post.post_id'), index=True)
    post_impressions = db.Column(db.Integer, index=True)
    post_consumptions = db.Column(db.Integer, index=True)
    post_impressions_unique = db.Column(db.Integer, index=True)

    def __init__(self, post_id, post_impressions, post_consumptions,
                 post_impressions_unique):
        self.post_id = post_id
        self.post_impressions = post_impressions
        self.post_consumptions = post_consumptions
        self.post_impressions_unique = post_impressions_unique

    def __repr__(self):
        return '<%s %s %s %s>' % (self.post_id, self.post_impressions,
                                            self.post_consumptions,self.post_impressions_unique)

