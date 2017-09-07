# -*- coding: utf-8 -*-
from tdg_social import ma
from tdg_social.schema.post import PostSchema

class TimeSchema(ma.Schema):
    time_of_day = ma.String()
    post_all = ma.Nested(PostSchema,many=True)

class DayTimeSchema(ma.Schema):
    day = ma.String()
    time_of_day = ma.Nested(TimeSchema,many=True)

class DayTime:
    def __init__(self,day, time_of_day):
        self.day = day
        self.time_of_day = time_of_day

    def __repr__(self):
        return '<%s, %s>' % (self.day, self.time_of_day)

class Time:
    def __init__(self,time_of_day,post_all):
        self.time_of_day = time_of_day
        self.post_all = post_all

    def __repr__(self):
        return '<%s, %s>' % (self.time_of_day, self.post_all)

day_time_schema = DayTimeSchema()