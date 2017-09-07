# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil import parser, tz
from tdg_social.utils.facebook import get_data,return_url,return_post_data,return_lcsp,async_calls,get_page_id
from tdg_social.models.channel import Channel
from tdg_social.models.post import Post
from tdg_social.constants.urls import APIs, Twitter_APIs
from tdg_social.constants.parameters import parameters
from flask_script import Command, Option


class AddPostFacebook(Command):
    def run(self):
        all_competitor_ids = [i.page_id for i in Channel.query.filter_by(type = 1).all()]
        today = datetime.today().replace(tzinfo = tz.gettz('UTC'))

        for id in all_competitor_ids:
            url = return_url(id, APIs['posts'])
            data = get_data(url,parameters)
            time.sleep(10)
            url_list = []
            for post in data['posts']['data']:
                if(int((today - parser.parse(post['created_time'])).days)<= 60):
                    url_list.append(return_url(post['id'],APIs['likes,comments,shares,attachments']))
            print("adding posts for page ", id)
            responses = async_calls(url_list)

            for i in range(0,len(responses)):
                obj = return_post_data(i,data)
                obj.update(return_lcsp(responses[i]))
                post_info = Post.query.filter_by(post_id = obj['post_id']).first()
                if not post_info:
                    post_info = Post(**obj)
                    post_info.save()
                else:
                    post_info.likes = obj['post_likes']
                    post_info.comments = obj['post_comments']
                    post_info.shares = obj['post_shares']
                    post_info.update()


from tdg_social.utils.twitter import return_post_data_twitter, return_url_twitter, get_data_twitter
import time


class AddPostTwitter(Command):
    def run(self):
        all_competitor_ids = [i.page_id for i in Channel.query.filter_by(type=2).all()]
        for id in all_competitor_ids:
            print("adding posts for ",id)
            url = return_url_twitter(id,Twitter_APIs['posts'],"-1")
            data = get_data_twitter(url)
            for post in data:
                obj = return_post_data_twitter(post)
                obj['page_id'] = Channel.query.filter_by(page_id = id).first().id
                post_info = Post.query.filter_by(post_id = obj['post_id']).first()
                if not post_info:
                    post_info = Post(**obj)
                    post_info.save()
                else:
                    post_info.post_likes = obj['post_likes']
                    post_info.post_shares = obj['post_shares']
                    post_info.update()
            time.sleep(30)
