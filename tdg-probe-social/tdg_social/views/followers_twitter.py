# -*- coding: utf-8 -*-
from flask import request
from tdg_social.apis.followers_twitter import follower_info
from tdg_social import app

@app.route("/followers", methods=['GET','POST'])
def get_followers():
    id = request.args.get('id')
    jsondata = follower_info(id)
    return jsondata
