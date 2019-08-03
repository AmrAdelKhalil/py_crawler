import requests

class Crawler:
	helper_keys = {
		'key': 'AIzaSyDVQ460q3wH1Hy2Gy4HQj4xVi6fVCeFBQ0'
	}

	base_urls = {
		'playlist_url': 'https://www.googleapis.com/youtube/v3/playlistItems',
		'video_url': 'https://www.googleapis.com/youtube/v3/videos',
		'playlist_by_channel_url': 'https://www.googleapis.com/youtube/v3/playlists'  
	}

	def videos_data_from_playlist(self, payload):
		response = requests.get(url = self.base_urls['playlist_url'], params = self.merge_key_to_payload(payload))
		return response.json()
		

	def playlist_items_for_channel(self, payload):
		response = requests.get(url = self.base_urls['playlist_by_channel_url'], params = self.merge_key_to_payload(payload))
		return response.json()

	def merge_key_to_payload(self, payload):
		payload.update(self.helper_keys)
		return payload

	def get_video_details(self, payload):
		response = requests.get(url = self.base_urls['video_url'], params = self.merge_key_to_payload(payload))
		return response.json()
