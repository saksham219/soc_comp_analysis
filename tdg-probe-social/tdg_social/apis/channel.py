# -*- coding: utf-8 -*-

from tdg_social.models.channel import Channel
from tdg_social.schema.channel import channel_schema
from tdg_social.utils.facebook import return_page_info
from tdg_social.utils.twitter import return_page_info_twitter
from flask import jsonify

def channel_add(channel_data):
    if 'channel' not in channel_data or 'page_id' not in channel_data:
        return jsonify({'errors': 'no channel or page_id specified'})
    if channel_data['channel'] == 1:
        obj = return_page_info(channel_data['page_id'])
    elif channel_data['channel'] == 2:
        obj = return_page_info_twitter(channel_data['page_id'])
    page_info = Channel.query.filter_by( page_id = channel_data['page_id']).first()
    obj['influencer'] = channel_data.get('influencer', False)
    obj['admin'] = channel_data.get('admin',False)
    if not page_info:
        page_info = Channel(**obj)
        page_info.save()
    else:
        page_info.page_name = obj['page_name']
        page_info.followers = obj['followers']
        page_info.following = obj['following']
        page_info.description = obj['description']
        page_info.website = obj['website']
        page_info.phone = obj['phone']
        page_info.influencer = obj['influencer']
        page_info.admin = obj['admin']
        page_info.update()
    return jsonify({'success':'page added'})

def channel_info(id, channel):
    page_info = Channel.query.filter_by(id = id, type = channel).first()
    if not page_info:
        return jsonify({'errrors':'page does not exist'})
    result = channel_schema.dump(page_info)
    return jsonify(result.data)

def channel_delete(id):
    page_info = Channel.query.filter_by(id = id).first()
    if not page_info:
        result = {'errors' : 'page does not exist'}
    else:
        page_info.delete()
        result = {'success':'page removed'}
    return jsonify(result)