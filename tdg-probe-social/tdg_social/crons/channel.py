# -*- coding: utf-8 -*-
from datetime import datetime
from tdg_social.models.channel import Channel
from tdg_social.utils.facebook import return_page_info
from tdg_social.utils.twitter import return_page_info_twitter
from tdg_social.constants.channel import ChannelListFacebook, ChannelListTwitter
from flask_script import Command

class AddChannelFacebook(Command):
    def run(self):
        print('adding competitors')
        for id in ChannelListFacebook:
            obj = return_page_info(id)
            competitor_info = Channel.query.filter_by(page_id = id).first()
            if not competitor_info :
                obj['influencer'] = False
                competitor_info = Channel(**obj)
                competitor_info.save()
            else:
                competitor_info.page_name = obj['page_name']
                competitor_info.type = obj['type']
                competitor_info.follewers = obj['followers']
                competitor_info.description = obj['description']
                competitor_info.website = obj['website']
                competitor_info.phone = obj['phone']
                competitor_info.update()


class AddChannelTwitter(Command):
    def run(self):
        print('adding competitors')
        for id in ChannelListTwitter:
            obj = return_page_info_twitter(id)
            obj['influencer'] = False
            competitor_info = Channel.query.filter_by(page_id = obj['page_id']).first()
            if not competitor_info :
                competitor_info = Channel(**obj)
                competitor_info.save()
            else:
                Channel.page_name = obj['page_name']
                competitor_info.followers = obj['followers']
                competitor_info.following = obj['following']
                competitor_info.description = obj['description']
                competitor_info.website = obj['website']
                competitor_info.update()
