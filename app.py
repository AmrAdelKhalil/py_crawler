from flask import request
from importers.crawler import *
from config.db import *
from models.videos import *
from presistors.presistor import *
from services.playlist_service import *

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
	return "here"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
