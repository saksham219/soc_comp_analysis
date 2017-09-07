# -*- coding: utf-8 -*-
from flask import request
from tdg_social.apis.hashtag import all_hashtag_facebook,post_hashtag_facebook,\
                                    all_hashtag_twitter,post_hashtag_twitter
from tdg_social import app

@app.route('/hashtag/facebook', methods = ['GET'])
def count_all_hashtag():
    obj = {
    'date_from' : request.args.get('date_from',''),
    'date_to' : request.args.get('date_to', '')
    }
    jsondata = all_hashtag_facebook(obj)
    return(jsondata)

@app.route('/hashtag/twitter', methods = ['POST', 'GET'])
def count_all_hashtag_twitter():
    obj ={
    'date_from' : request.args.get('date_from'),
    'date_to' : request.args.get('date_to'),
    'influencer' : bool(request.args.get('influencer'))
    }
    jsondata = all_hashtag_twitter(obj)
    return(jsondata)

@app.route('/hashtag/<string:hashtag>/facebook', methods = ['GET'])
def post_specific_hashtag_facebook(hashtag):
    obj={
    'date_from' : request.args.get('date_from'),
    'date_to' : request.args.get('date_to'),
    'id' : request.args.get('id'),
    'type' : request.args.get('type'),
    'sortby' : request.args.get('sortby'),
    }
    jsondata = post_hashtag_facebook(hashtag,obj)
    return(jsondata)

@app.route('/hashtag/<string:hashtag>/twitter', methods = ['GET'])
def post_specific_hashtag_twitter(hashtag):
    obj={
    'date_from' : request.args.get('date_from'),
    'date_to' : request.args.get('date_to'),
    'influencer':bool(request.args.get('influencer')),
    'id' : request.args.get('id'),
    'type' : request.args.get('type'),
    'sortby' : request.args.get('sortby'),
    }
    jsondata = post_hashtag_twitter(hashtag,obj)
    return(jsondata)
