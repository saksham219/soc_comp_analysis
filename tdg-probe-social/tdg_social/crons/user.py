from tdg_social.models.user import User
from tdg_social.models.channel import Channel
from tdg_social.constants.urls import Twitter_APIs
from tdg_social.utils.twitter import return_url_twitter,get_data_twitter,return_user_data_twitter,get_cursor_data
from flask_script import Command, Option

class AddUserTwitter(Command):
    def run(self):
        page_id_obj = Channel.query.filter(Channel.page_id.notin_(set([i.page_id for i in User.query.join(Channel).all()])),Channel.type==2).first()
        if page_id_obj:
            page_id = page_id_obj.page_id
        else:
            page_id = min({i:Channel.query.filter_by(page_id= i).first().created_at for i in set([i.page_id for i in User.query.join(Channel).all()])})
        print(page_id)
        url = return_url_twitter(page_id,Twitter_APIs['followers'],"-1")
        data = get_data_twitter(url)
        cursor_data = get_cursor_data(data,page_id,[])
        [data['users'].append(user) for user in cursor_data]
        for user in data['users']:
            obj = return_user_data_twitter(user)
            obj['page_id'] = page_id
            user_info = User.query.filter_by(user_id=obj['user_id'],page_id=obj['page_id']).first()
            if not user_info:
                user_info = User(**obj)
                user_info.save()
            else:
                user_info.user_description = obj['user_description']
                user_info.user_name = obj['user_name']
                user_info.user_screen_name = obj['user_screen_name']
                user_info.user_photo = obj['user_photo']
                user_info.update()
