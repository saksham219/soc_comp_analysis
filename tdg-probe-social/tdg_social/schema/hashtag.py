# -*- coding: utf-8 -*-
from tdg_social import ma

class HashtagSchema(ma.Schema):
    hashtag = ma.Str()
    count = ma.Int()

class Hashtag:
    def __init__(self,hashtag,count):
        self.hashtag = hashtag
        self.count = count
    def __repr__(self):
        return '<%s %s>' % (self.hashtag, self.count)

hashtags_schema = HashtagSchema(many=True)
hashtag_schema = HashtagSchema()