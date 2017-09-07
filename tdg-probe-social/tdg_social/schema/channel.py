# -*- coding: utf-8 -*-
from tdg_social import ma


class ChannelSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type', 'page_id', 'page_name', 'followers', 'following', 'description',
                  'website', 'phone', 'admin', 'influencer', 'created_at', 'updated_at')
        exclude = ('created_at', 'updated_at', 'id')


channel_schema = ChannelSchema()