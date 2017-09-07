# -*- coding: utf-8 -*-
from tdg_social.models.post import Post
from tdg_social.models.channel import Channel
from tdg_social.schema.post import post_schema,post_schemas
from tdg_social.schema.day_time_classify import Time, DayTime, day_time_schema
from tdg_social.utils.api import get_local_time, split_day_by_hour
from flask import jsonify
import calendar
from sqlalchemy.sql import extract

def post_info_facebook(obj):
    competitor_list = [i.id for i in Channel.query.filter_by(type = 1,influencer = False).all()]
    if obj['post_id']:
        result = post_schema.dump(Post.query.filter(Post.post_id==obj['post_id']).first())
    else:
        filters = ((Post.page_id.in_(competitor_list)),)
        if obj['id']: filters += (Post.page_id == obj['id'],)
        if obj['type'] : filters += (Post.post_type == obj['type'],)
        if obj['date_from'] and obj['date_to']:
            filters += (Post.post_created_time >= get_local_time(int(obj['date_from'])),
                        Post.post_created_time<=get_local_time(int(obj['date_to'])),)
        sortby = 'post_'+obj['sortby']+' desc' if obj['sortby'] else ''
        post_filter = Post.query.filter(*filters).order_by(sortby).all()
        result = post_schemas.dump(post_filter)
    return jsonify(result.data)


def day_time_facebook(obj):
    if not obj['day']:return jsonify({'error':'enter day of week'})
    else:
        competitor_list = [i.id for i in Channel.query.filter_by(type=1, influencer=False).all()]
        hours_of_day = split_day_by_hour(obj['hour_period']) if obj['hour_period'] else split_day_by_hour('2')
        time_obj_list = []
        for i in hours_of_day:
            filters = ((Post.page_id.in_(competitor_list)),)
            if obj['id']: filters += (Post.page_id == obj['id'],)
            if obj['type']: filters += (Post.post_type == obj['type'],)
            if obj['date_from'] and obj['date_to']:
                filters += (Post.post_created_time >= get_local_time(int(obj['date_from'])),
                            Post.post_created_time <= get_local_time(int(obj['date_to'])),)
            filters +=  (extract('dow',Post.post_created_time)==obj['day'],)
            filters += (extract('hour',Post.post_created_time) >=i[0],
                        extract('hour',Post.post_created_time) < i[1])
            sortby = 'post_' + obj['sortby'] + ' desc' if obj['sortby'] else ''
            post_filter = Post.query.filter(*filters).order_by(sortby).all()
            time_obj_list.append(Time(str(i[0])+ '-' + str(i[1]),post_filter))
        object_info = DayTime(obj['day'],time_obj_list)
        result = day_time_schema.dump(object_info)
        return jsonify(result)

def post_info_twitter(obj):
    competitor_list = [i.id for i in Channel.query.filter_by(type = 2,influencer = False).all()]
    influencer_list = [i.id for i in Channel.query.filter_by(type=2,influencer = True).all()]
    if obj['post_id']:
        result = post_schema.dump(Post.query.filter(Post.post_id==obj['post_id']).first())
    else:
        filters = ()
        if obj['influencer'] ==True : filters+= (Post.page_id.in_(influencer_list),)
        else: filters+= (Post.page_id.in_(competitor_list),)
        if obj['id']: filters += (Post.page_id == obj['id'],)
        if obj['type']: filters += (Post.post_type == obj['type'],)
        if obj['date_from'] and obj['date_to']:
            filters += (Post.post_created_time >= get_local_time(int(obj['date_from'])),
                        Post.post_created_time <= get_local_time(int(obj['date_to'])),)
        sortby = 'post_' + obj['sortby'] + ' desc' if obj['sortby'] else ''
        post_filter = Post.query.filter(*filters).order_by(sortby).all()
        result = post_schemas.dump(post_filter)
    return jsonify(result.data)

def day_time_twitter(obj):
    if not obj['day']:return jsonify({'error':'enter day of week'})
    else:
        competitor_list = [i.id for i in Channel.query.filter_by(type=2, influencer=False).all()]
        influencer_list = [i.id for i in Channel.query.filter_by(type=2, influencer=True).all()]
        hours_of_day = split_day_by_hour(obj['hour_period']) if obj['hour_period'] else split_day_by_hour('2')
        time_obj_list = []
        for i in hours_of_day:
            filters =()
            if obj['influencer'] == True:filters += (Post.page_id.in_(influencer_list),)
            else: filters += (Post.page_id.in_(competitor_list),)
            if obj['id']: filters += (Post.page_id == obj['id'],)
            if obj['type']: filters += (Post.post_type == obj['type'],)
            if obj['date_from'] and obj['date_to']:
                filters += (Post.post_created_time >= get_local_time(int(obj['date_from'])),
                            Post.post_created_time <= get_local_time(int(obj['date_to'])),)
            filters +=  (extract('dow',Post.post_created_time)==obj['day'],)
            filters += (extract('hour',Post.post_created_time) >=i[0],
                        extract('hour',Post.post_created_time) < i[1])
            sortby = 'post_' + obj['sortby'] + ' desc' if obj['sortby'] else ''
            post_filter = Post.query.filter(*filters).order_by(sortby).all()
            print(post_filter)
            time_obj_list.append(Time(str(i[0])+ '-' + str(i[1]),post_filter))
        object_info = DayTime(obj['day'],time_obj_list)
        result = day_time_schema.dump(object_info)
        return jsonify(result)