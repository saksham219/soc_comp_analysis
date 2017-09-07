# -*- coding: utf-8 -*-
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('../config.cfg')
ma = Marshmallow(app)

db = SQLAlchemy(app)

import tdg_social.views.channel
import tdg_social.views.hashtag
import tdg_social.views.post
import tdg_social.views.followers_twitter

from tdg_social.models.channel import Channel
from tdg_social.models.user import User
from tdg_social.models.post import Post,PostInsight
from tdg_social.models.like import Like
from tdg_social.models.comment import Comment
from tdg_social.models.photo import Photo
from tdg_social.models.hash import Hash

db.create_all()