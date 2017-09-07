# -*- coding: utf-8 -*-
from tdg_social.models.post import Post
from tdg_social.models.channel import Channel
from tdg_social.models.hash import Hash
from tdg_social.utils.api import get_local_time
from tdg_social.schema.hashtag import Hashtag,hashtags_schema,hashtag_schema
from tdg_social.schema.post import post_schemas
from flask import jsonify
from tdg_social import db

def all_hashtag_facebook(obj):
    competitor_list = [i.id for i in Channel.query.filter_by(type = 1,influencer = False).all()]
    filters = ((Post.page_id.in_(competitor_list)),)
    if obj['date_from'] and obj['date_to']:
        filters += (Post.post_created_time >= get_local_time(int(obj['date_from'])),
                    Post.post_created_time <= get_local_time(int(obj['date_to'])),)
    obj_list = []
    for i in db.session.query(Hash.hashtag,db.func.count(Post.id)).join(Post.hashtags).filter(*filters).group_by(Hash.hashtag).all():
        obj_list.append(Hashtag(*i))
    result = hashtags_schema.dump(obj_list)
    return jsonify(result.data)


def post_hashtag_facebook(hashtag,obj):
    competitor_list = [i.id for i in Channel.query.filter_by(type = 1,influencer = False).all()]
    filters = ((Post.page_id.in_(competitor_list)),)
    if obj['id']: filters += (Post.page_id == obj['id'],)
    if obj['type'] : filters += (Post.post_type == obj['type'],)
    if obj['date_from'] and obj['date_to']:
        filters += (Post.post_created_time >= get_local_time(int(obj['date_from'])),
                        Post.post_created_time<=get_local_time(int(obj['date_to'])),)
    filters += ((Hash.hashtag== hashtag),)
    sortby = 'post_'+obj['sortby']+' desc' if obj['sortby'] else ''
    post_filter = Post.query.join(Hash.posts).filter(*filters).order_by(sortby).all()
    result = post_schemas.dump(post_filter)
    return jsonify(result.data)


def all_hashtag_twitter(obj):
    competitor_list = [i.id for i in Channel.query.filter_by(type=2, influencer=False).all()]
    influencer_list = [i.id for i in Channel.query.filter_by(type=2,influencer = True).all()]
    filters = ()
    if obj['influencer'] == True: filters += (Post.page_id.in_(influencer_list),)
    else: filters += (Post.page_id.in_(competitor_list),)
    if obj['date_from'] and obj['date_to']:
        filters += (Post.post_created_time >= get_local_time(int(obj['date_from'])),
                    Post.post_created_time <= get_local_time(int(obj['date_to'])),)
    obj_list = []
    for i in db.session.query(Hash.hashtag,db.func.count(Post.id)).join(Post.hashtags).filter(*filters).group_by(Hash.hashtag).all():
        obj_list.append(Hashtag(*i))
    result = hashtags_schema.dump(obj_list)
    return jsonify(result.data)


def post_hashtag_twitter(hashtag,obj):
    competitor_list = [i.id for i in Channel.query.filter_by(type = 2,influencer = False).all()]
    influencer_list = [i.id for i in Channel.query.filter_by(type=2,influencer = True).all()]
    filters = ()
    if obj['influencer'] == True: filters += (Post.page_id.in_(influencer_list),)
    else: filters += (Post.page_id.in_(competitor_list),)
    if obj['id']: filters += (Post.page_id == obj['id'],)
    if obj['type']: filters += (Post.post_type == obj['type'],)
    if obj['date_from'] and obj['date_to']:
        filters += (Post.post_created_time >= get_local_time(int(obj['date_from'])),
                    Post.post_created_time <= get_local_time(int(obj['date_to'])),)
    filters += ((Hash.hashtag == hashtag),)
    sortby = 'post_' + obj['sortby'] + ' desc' if obj['sortby'] else ''
    post_filter = Post.query.join(Hash.posts).filter(*filters).order_by(sortby).all()
    result = post_schemas.dump(post_filter)
    return jsonify(result.data)