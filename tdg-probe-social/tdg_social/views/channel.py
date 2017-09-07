# -*- coding: utf-8 -*-
from flask import request
from tdg_social.apis.channel import channel_add, channel_info,channel_delete
from tdg_social import app

@app.route("/channel", methods=['POST', 'GET'])
def add_channel():
	if request.method == 'POST':
		data = request.get_json()
		jsondata = channel_add(data)
		return jsondata
	else:
		channel = request.args.get('channel')
		id = request.args.get('id')
		jsondata = channel_info(id,channel)
		return jsondata

@app.route("/channel/<int:id>", methods = ['DELETE'])
def delete_channel(id):
	jsondata = channel_delete(id)
	return jsondata