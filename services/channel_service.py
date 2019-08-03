from importers.crawler import *

class ChannelService:
	def __init__(self, payload={}):
		self.payload = {'part': 'snippet', 'maxResults': 1}
		self.payload.update(payload)

	def get_playlists(self):
		items = []
		while(True):
			result = Crawler().playlist_items_for_channel(self.payload)
			for idx in range(len(result['items'])):
				items += [result['items'][idx]['id']]
			break;
			if (('nextPageToken' in result) == False):
				break
			else:
				self.payload.update({'pageToken': result['nextPageToken']})

		return items
