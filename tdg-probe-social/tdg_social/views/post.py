# -*- coding: utf-8 -*-
from flask import request
from tdg_social.apis.post import post_info_facebook,post_info_twitter,\
                                day_time_facebook,day_time_twitter
from tdg_social import app

@app.route('/post/facebook',methods = ['GET'])
def return_post_data():
    obj = {
        'post_id' : request.args.get('post_id'),
        'date_from' : request.args.get('date_from'),
        'date_to' : request.args.get('date_to'),
        'id' : request.args.get('id'),
        'type' : request.args.get('type'),
        'sortby' : request.args.get('sortby')
    }
    jsondata = post_info_facebook(obj)
    return jsondata 

@app.route('/postdaytime/facebook', methods = ['GET'])
def post_day_time_facebook():
    obj = {
    'date_from' : request.args.get('date_from'),
    'date_to' : request.args.get('date_to'),
    'day' : request.args.get('day'),
    'hour_period' : request.args.get('hour_period'),
    'id' : request.args.get('id'),
    'type' : request.args.get('type'),
    'sortby':request.args.get('sortby')
    }
    jsondata = day_time_facebook(obj)
    return jsondata 


@app.route('/post/twitter',methods = ['GET'])
def return_post_day_twitter():
    obj = {
        'post_id': request.args.get('post_id'),
        'date_from': request.args.get('date_from'),
        'date_to': request.args.get('date_to'),
        'influencer':bool(request.args.get('influencer')),
        'id': request.args.get('id'),
        'type': request.args.get('type'),
        'sortby': request.args.get('sortby')
    }
    jsondata = post_info_twitter(obj)
    return jsondata 

@app.route('/postdaytime/twitter', methods = ['GET'])
def classify_date_time_twitter():
    obj = {
    'date_from' : request.args.get('date_from'),
    'date_to' : request.args.get('date_to'),
    'day' : request.args.get('day'),
    'hour_period' : request.args.get('hour_period'),
    'influencer' : bool(request.args.get('influencer')),
    'id' : request.args.get('id'),
    'type' : request.args.get('type'),
    'sortby': request.args.get('sortby')
    }
    jsondata = day_time_twitter(obj)
    return jsondata 
