from importers.crawler import *
from models.videos import *
from services.playlist_service import *

class Presistor:
	def __init__(self, items):
		self.items = items

	def get_extra_data(self, new_record, video_id):
		payload = {'part': 'statistics,contentDetails', 'id': video_id}
		data = Crawler().get_video_details(payload)
		new_record.duration = data['items'][0]['contentDetails']['duration']
		new_record.views = data['items'][0]['statistics']['viewCount']
		return new_record

	def presist_data(self):
		for idx in range(len(self.items)):
			new_record = Videos(video_url = 'https://www.youtube.com/watch?v=' + self.items[idx]['snippet']['resourceId']['videoId'],title = self.items[idx]['snippet']['title'], image = self.items[idx]['snippet']['thumbnails']['default']['url'], thumbnail = self.items[idx]['snippet']['thumbnails']['medium']['url'])
			new_record = self.get_extra_data(new_record, self.items[idx]['snippet']['resourceId']['videoId'])
			new_record.downloaded_thumbnail_path = ''
			new_record.downloaded_image_path = ''
			db.session.add(new_record)
		
		db.session.commit()
