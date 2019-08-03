from importers.crawler import *

class PlaylistService:
	def __init__(self, payload={}):
		self.payload = {'part': 'snippet', 'maxResults': 1}
		self.payload.update(payload)

	def get_playlist_items(self):
		items = []
		while(True):
			result = Crawler().videos_data_from_playlist(self.payload)
			items += result['items']
			break;
			if (('nextPageToken' in result) == False):
				break
			else:
				self.payload.update({'pageToken': result['nextPageToken']})

		return items
