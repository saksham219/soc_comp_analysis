# -*- coding: utf-8 -*-
from tdg_social import app

token = app.config['FACEBOOK_APP_ID'] + '|' + app.config['FACEBOOK_APP_SECRET']
parameters = {'period': '', 'access_token':token}

consumer_key = app.config['TWITTER_CONSUMER_KEY']
consumer_secret = app.config['TWITTER_CONSUMER_SECRET']