# -*- coding: utf-8 -*-
APIs = {'likes,comments,photos': '?fields=likes.limit(500),comments.limit(500),attachments.limit(50)',
        'posts': '?fields=posts.limit(700){created_time,message,link,type}&since=2017-04-14&until=now',
        'page_info': '?fields=fan_count,description,website,phone,name',
        'insights': '?fields=insights.metric(post_impressions, post_consumptions, post_impressions_unique)',
        'likes,comments,shares,attachments': '?fields=shares,likes.limit(0).summary(true),comments.limit(0).summary(true),attachments'}

Twitter_APIs = {'posts': 'statuses/user_timeline.json?count=200&trim_user=1&user_id=',
                'page_info': 'users/show.json?user_id=',
                'followers': 'followers/list.json?&count=200&include_entities=false&user_id='}