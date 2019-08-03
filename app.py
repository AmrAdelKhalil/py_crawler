from flask import request
from importers.crawler import *
from config.db import *
from models.videos import *
from presistors.presistor import *

@app.route('/')
def hello():
    return "Welcome to my little application"

@app.route('/playlist')
def set_videos_info_using_playlist():
	playlist_id = request.args.get('playlist_url')
	payload = {'part': 'snippet', 'maxResults': 1}
	payload.update({'playlistId': playlist_id})
	items = []
	while(True):
		result = Crawler().videos_data_from_playlist(payload)
		items += result['items']
		break;
		if (('nextPageToken' in result) == False):
			break
		else:
			payload.update({'pageToken': result['nextPageToken']})

	Presistor(items).presist_data(items)
	return 'Videos data have been fetched successfully!!!'

@app.route('/channel')
def set_videos_info_using_channel():
	return "here"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
