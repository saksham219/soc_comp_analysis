# -*- coding: utf-8 -*-
from tdg_social import ma

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id','post_id','post_type', 'post_created_time','post_content','post_link',
                  'post_likes','post_comments','post_shares','post_photos','created_at','updated_at','page_id')
        exclude = ('created_at', 'updated_at', 'id')
    post_created_time= ma.DateTime('%Y-%m-%dT%H:%M:%S+05:30')

post_schema = PostSchema()
post_schemas = PostSchema(many=True)