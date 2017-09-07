# -*- coding: utf-8 -*-
from tdg_social import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'user_name', 'user_screen_name', 'user_description',
                  'user_photo', 'page_id', 'created_at', 'updated_at')
        exclude = ('page_id', 'created_at', 'updated_at', 'id')


class FollowerSchema(ma.Schema):
    competitor_influencer_name = ma.Str()
    followers = ma.Nested(UserSchema, many=True)


class Follower:
    def __init__(self, competitor_influencer_name, followers):
        self.competitor_influencer_name = competitor_influencer_name
        self.followers = followers

    def __repr__(self):
        return '<%s %s>' % (self.competitor_influencer_name, self.followers)

follower_schema = FollowerSchema()
