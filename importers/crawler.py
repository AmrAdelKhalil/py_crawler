import requests

class Crawler:
	helper_keys = {
		'key': 'AIzaSyDVQ460q3wH1Hy2Gy4HQj4xVi6fVCeFBQ0'
	}

	base_urls = {
		'playlist_url': 'https://www.googleapis.com/youtube/v3/playlistItems',
		'video_url': 'https://www.googleapis.com/youtube/v3/videos',
		'channel_url': ''  
	}

	# , playlistId='PLvFsG9gYFxY_2tiOKgs7b2lSjMwR89ECb', page_token=''	
	# {'part': 'snippet', 'key': helper_keys['key'], playlistId: , 'maxResult': helper_keys['max_result']}

	def videos_data_from_playlist(self, payload):
		response = requests.get(url = self.base_urls['playlist_url'], params = self.merge_key_to_payload(payload))
		return response.json()
		

	def playlist_ids_for_channel(self, payload):
		# call the api that gives you the playlist id
		return "toto"

	def merge_key_to_payload(self, payload):
		payload.update(self.helper_keys)
		return payload

	def get_video_details(self, payload):
		response = requests.get(url = self.base_urls['video_url'], params = self.merge_key_to_payload(payload))
		return response.json()
