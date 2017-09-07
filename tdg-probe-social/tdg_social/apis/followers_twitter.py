# -*- coding: utf-8 -*-
from tdg_social.models.channel import Channel
from tdg_social.schema.user import Follower, follower_schema
from tdg_social.models.user import User
from tdg_social.utils.api import get_page_name
from flask import jsonify


def follower_info(id):
    user_list = User.query.join(Channel).filter(Channel.id==id).all()
    page_name = get_page_name(id)
    object_info_list = Follower(page_name, user_list)
    result = follower_schema.dump(object_info_list)
    return jsonify(result.data)
