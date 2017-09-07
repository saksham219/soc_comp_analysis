# -*- coding: utf-8 -*-
from tdg_social.constants.parameters import consumer_key, consumer_secret
from tdg_social.constants.base import twitter_base
from tdg_social.constants.urls import Twitter_APIs
from tdg_social.utils.api import return_datestamp
import oauth2 as oauth
import json
import time


def return_url_twitter(id,api_req,cursor):
    node = api_req + id + '&cursor=' + cursor
    url = twitter_base+node
    return(url)

def get_data_twitter(url):
    consumer = oauth.Consumer(key=consumer_key,secret=consumer_secret)
    request_token_url = url
    client = oauth.Client(consumer)
    resp,content = client.request(request_token_url, "GET")
    content = content.decode("utf-8")
    data = json.loads(content)
    return(data)

def return_page_info_twitter(id):
    url = return_url_twitter(id,Twitter_APIs['page_info'],"-1")
    data = get_data_twitter(url)
    return_obj = {
        'type' :2,
        'page_id' : data['id_str'],
        'page_name' : data['name'],
        'followers' : data['followers_count'],
        'following' : data['friends_count'],
        'description': data['description'],
        'website': data['url'],
        'admin' : True if id == "3793903573" else False,
        'phone' : ""
    }
    return return_obj

def return_post_data_twitter(data):
    photos =[]
    post_link=''
    if data['entities']['urls'] != [] and 'media' not in data['entities']:
        post_type = 'link'
        post_link = data['entities']['urls'][0]['expanded_url']
    elif 'media' in data['entities']:
        post_type = data['entities']['media'][0]['type']
        photos.append(data['entities']['media'][0]['media_url_https'])
        if data['entities']['urls'] != []:
            post_link = data['entities']['urls'][0]['expanded_url']
    else:
        post_type = 'status'
    return_obj = {
        'post_id' : data['id_str'],
        'post_type': post_type,
        'post_created_time' : return_datestamp(data['created_at']),
        'post_link' : post_link,
        'post_photos' : photos,
        'post_content' : data['text'],
        'post_likes' : data['favorite_count'],
        'post_comments' : 0,
        'post_shares' : data['retweet_count'],
    }
    return return_obj


def return_user_data_twitter(data):
    return_obj = {
        'user_id' : data['id_str'],
        'user_name' : data['name'],
        'user_screen_name' : data['screen_name'],
        'user_description' : data['description'],
        'user_photo' : data['profile_image_url_https']
    }
    return return_obj

def get_cursor_data(data, id, user_list):
    if data['next_cursor_str'] != '0':
        print("adding followers")
        time.sleep(60)
        cursor = data['next_cursor_str']
        url = return_url_twitter(id, 'followers/list.json?&count=200&include_entities=false&user_id=', cursor)
        data_new = get_data_twitter(url)
        [user_list.append(user) for user in data_new['users']]
        data_new = get_cursor_data(data_new, id, user_list)
    return user_list

