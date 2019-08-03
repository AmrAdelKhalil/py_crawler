from flask import request
from flask import jsonify
from importers.crawler import *
from config.db import *
from models.videos import *
from presistors.presistor import *
from services.playlist_service import *
from services.channel_service import *
import urllib2
from scheduleCron import run_cron

@app.route('/')
def hello():
    return "Welcome to my little application"

@app.route('/playlist')
def set_videos_info_using_playlist():
	items = PlaylistService({'playlistId': request.args.get('playlist_url')}).get_playlist_items()
	Presistor(items).presist_data()
	return 'Videos data have been fetched successfully!!!'

@app.route('/channel')
def set_videos_info_using_channel():
	playlist_ids = ChannelService({'channelId': request.args.get('channel_id')}).get_playlists()
	items = []
	for idx in range(len(playlist_ids)):
		items += PlaylistService({'playlistId': playlist_ids[idx]}).get_playlist_items()
	Presistor(items).presist_data()
	return 'Videos data have been fetched successfully!!!'

@app.route('/list_videos')
def get_all_videos():
	data = Videos.query.all()
	response = []
 	for idx in range(len(data)):
 		response += [{'id': data[idx].id, 'title': data[idx].title, 'duration': data[idx].duration, 'views': data[idx].views, 'url': data[idx].video_url, 'tumbnail': data[idx].thumbnail, 'full-sized-image': data[idx].image, 'local-thumbnail-path': data[idx].downloaded_thumbnail_path, 'local-image-path': data[idx].downloaded_image_path}]
	return jsonify({'data': response})

if __name__ == "__main__":
	run_cron()
	app.run(host="0.0.0.0", debug=True, use_reloader=False)
