# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil import parser,tz
from tdg_social.models.post import Post, PostInsight
from tdg_social.models.channel import Channel
from tdg_social.utils.facebook import return_url, async_calls, return_insights
from tdg_social.constants.urls import APIs
from flask_script import Command, Option

class AddInsightFacebook(Command):
    def run(self):
        our_post = Post.query.filter(Post.page_id.in_([i.id for i in Channel.query.filter_by(type=1,admin=True)])).all()

        today = datetime.today().replace(tzinfo = tz.gettz('UTC'))
        our_post_ids = [post.post_id for post in our_post if int((today - post.post_created_time).days)<= 60]
        url_list = [return_url(id, APIs['insights']) for id in our_post_ids]
        print('adding insights')
        result = async_calls(url_list)
        for data in result:
            try:
                obj = return_insights(data)
            except:
                print('ACCESS TOKEN DOES NOT HAVE PERMISSIONS TO LOAD INSIGHTS')
                break
            post_info = PostInsight.query.filter_by(post_id = obj['post_id']).first()
            if not post_info:
                post_info = PostInsight(**obj)
                post_info.save()
            else:
                post_info.post_impressions = obj['post_impressions']
                post_info.post_consumptions = obj['post_consumptions']
                post_info.post_impressions_unique = obj['post_impressions_unique']
                post_info.update()


