# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil import parser, tz
from tdg_social.models.post import Post
from tdg_social.models.like import Like
from tdg_social.models.comment import Comment
from tdg_social.models.photo import Photo
from tdg_social.utils.facebook import return_url, async_calls, check_paging_likes, breaker_url,\
                                        return_user_like, return_user_comment, return_post_photo
from tdg_social.constants.urls import APIs
from flask_script import Command, Option

class AddLcpFacebook(Command):
    def run(self):
        all_post = Post.query.order_by(Post.post_id).all()
        today = datetime.today().replace(tzinfo = tz.gettz('UTC'))
        all_post_ids = [post.post_id for post in all_post if int((today - post.post_created_time).days) < 31]
        url_list = [return_url(id, APIs['likes,comments,photos']) for id in all_post_ids]

        url_list_break = breaker_url(url_list)

        for i in url_list_break:
            results = async_calls(i)
            for data in results:
                post_id = data['id']
                print(post_id)
                data['likes'] = check_paging_likes(data['likes'])
                likes_count = len(data['likes']['data']) if 'likes' in data else 0
                comments_count = len(data['comments']['data']) if 'comments' in data else 0
                photos_count = len(Post.query.filter(Post.post_id == post_id).first().post_photos)
                print('adding likes')

                for j in range(0,likes_count):
                    obj = return_user_like(data['likes'],j)
                    obj['post_id'] = post_id
                    like_info = Like.query.filter_by(post_id = obj['post_id'], user_id = obj['user_id']).first()
                    if not like_info:
                        like_info = Like(**obj)
                        like_info.save()

                print('adding comments')
                for j in range(0,comments_count):
                    obj = return_user_comment(data['comments'],j)
                    obj['post_id'] = post_id
                    comment_info = Comment.query.filter_by(post_id = obj['post_id'], user_id = obj['user_id']).first()
                    if not comment_info:
                        comment_info = Comment(**obj)
                        comment_info.save()

                if(photos_count==1):
                    print('adding photos')
                    obj = return_post_photo(data['attachments'])
                    obj['post_id'] = post_id
                    photo_info = Photo.query.filter_by(post_id = obj['post_id'], photo = obj['photo']).first()
                    if not photo_info:
                        photo_info = Photo(**obj)
                        photo_info.save()

                else:
                    print('adding photos')
                    for j in range(0,photos_count):
                        obj = return_post_photo(data['attachments']['data'][0]['subattachments'])
                        obj['post_id'] = post_id
                        photo_info = Photo.query.filter_by(post_id =obj['post_id'], photo = obj['photo']).first()
                        if not photo_info:
                            photo_info = Photo(**obj)
                            photo_info.save()


