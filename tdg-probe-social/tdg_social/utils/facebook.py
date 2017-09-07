# -*- coding: utf-8 -*-
import requests
import asyncio
from aiohttp import ClientSession
from tdg_social.constants.base import base
from tdg_social.constants.parameters import parameters
from tdg_social.constants.urls import APIs
from tdg_social.models.channel import Channel
from tdg_social.utils.api import return_datestamp

def get_data(url, parameters):
    data = requests.get(url,params=parameters).json()
    return(data)

def return_url(id, api_req):
        node ='/'+ id + api_req
        url = base + node
        return(url)

def get_page_id(post_id):
    page_id = Channel.query.filter(Channel.page_id == post_id.split('_')[0]).first().id
    return(page_id)

def return_page_info(id):
    if(id == '763865327072658'):
        admin= True
    else:
        admin = False
    url = return_url(id, APIs['page_info'])
    data = get_data(url, parameters)
    return_obj = {
        'type' : 1,
        'page_id': data['id'],
        'page_name': data['name'],
        'followers': data['fan_count'],
        'following': 0,
        'description': data.get('description', ''),
        'phone': data.get('phone', ''),
        'website': data.get('website',''),
        'admin': admin
    }
    return return_obj

def return_post_data(i,data):
    return_obj = {
        'post_id' : data['posts']['data'][i]['id'],
        'post_type' :data['posts']['data'][i]['type'],
        'post_created_time' : return_datestamp(data['posts']['data'][i]['created_time']),
        'post_content' : data['posts']['data'][i]['message'] if 'message' in data['posts']['data'][i] else '',
        'post_link' : data['posts']['data'][i]['link'] if 'link' in data['posts']['data'][i] else '',
        'page_id' : get_page_id(data['posts']['data'][i]['id'])
    }
    return return_obj

def return_lcsp(data):#LikeCommentSharesPhotos
    photos = []
    if 'attachments' in data:
        if(data['attachments']['data'][0]['type'] == 'album'):
            for m in range(0,len( data['attachments']['data'][0]['subattachments']['data'])):
                photos.append(data['attachments']['data'][0]['subattachments']['data'][m]['media']['image']['src'])
        else:
            if('media' in data['attachments']['data'][0]):
                photos.append(data['attachments']['data'][0]['media']['image']['src'])
    return_obj = {
        'post_likes': data['likes']['summary']['total_count'] if 'likes' in data else 0,
        'post_comments': data['comments']['summary']['total_count'] if 'comments' in data else 0,
        'post_shares' : data['shares']['count'] if 'shares' in data else 0,
        'post_photos' : photos
    }
    return return_obj

def async_calls(url_list):
    async def fetch(url,requests):
        async with requests.get(url,params = parameters) as response:
            return await response.json()

    async def run(r):
        tasks=[]
        async with ClientSession() as session:
            for i in range(len(url_list)):
                task = asyncio.ensure_future(fetch(url_list[i], session))
                tasks.append(task)
            responses = await asyncio.gather(*tasks)
            future.set_result(responses)

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(10))
    loop.run_until_complete(future)
    return(future.result())

def check_paging_likes(data):
    if 'next' in data['paging']:
        url = data['paging']['next']
        data_new = requests.get(url, params=parameters).json()
        for user_info in data_new['data']:
            data['data'].append(user_info)
    return(data)

def breaker_url(url_list):
    urls_break = []
    for add_count in range(0,int(len(url_list)/400)):
        if(add_count == int(len(url_list)/400)-1):
            urls_break.append(url_list[add_count*400:])
        else:
            urls_break.append(url_list[add_count*400: add_count*400+400])
    return(urls_break)

def return_insights(data):
    return_obj = {
        'post_id' : data['id'],
        'post_impressions' : data['insights']['data'][0]['values'][0]['value'],
        'post_consumptions' : data['insights']['data'][1]['values'][0]['value'],
        'post_impressions_unique' : data['insights']['data'][2]['values'][0]['value']
    }
    return return_obj



def return_user_like(data,j):
    return_obj = {
        'user_id' : data['data'][j]['id'],
        'user_name':data['data'][j]['name']
    }
    return return_obj

def return_user_comment(data,j):
    return_obj = {
        'user_id' : data['data'][j]['from']['id'],
        'user_name': data['data'][j]['from']['name'],
        'user_message': data['data'][j]['message'],
        'user_created_time' : data['data'][j]['created_time']
    }
    return return_obj

def return_post_photo(data,j=None):
    if j ==None:
        return_obj = {
            'photo_desc': data['data'][0]['description'] if 'description' in data['data'][0] else "",
            'photo' : data['data'][0]['media']['image']['src'] if 'media' in data['data'][0] else "",
        }
    else:
        return_obj = {
            'photo_desc' : data['data'][j]['description'] if 'description' in da['data'][0]['subattachments']['data'][m] else "",
            'photo' : data['data'][j]['media']['image']['src'] if 'media' in data['attachments']['data'][0]['subattachments']['data'][m] else ""
        }
    return return_obj
