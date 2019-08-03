from importers.crawler import *
from models.videos import *

class Presistor:
	def __init__(self, items):
		self.videos_data = items

	def get_extra_data(self, new_record, video_id):
		payload = {'part': 'statistics,contentDetails', 'id': video_id}
		data = Crawler().get_video_details(payload)
		new_record.duration = data['items'][0]['contentDetails']['duration']
		new_record.views = data['items'][0]['statistics']['viewCount']
		return new_record

	def presist_data(self, items):
		for idx in range(len(items)):
			new_record = Videos(video_url = 'https://www.youtube.com/watch?v=' + items[idx]['snippet']['resourceId']['videoId'],title = items[idx]['snippet']['title'], image = items[idx]['snippet']['thumbnails']['default']['url'], thumbnail = items[idx]['snippet']['thumbnails']['medium']['url'])
			new_record = self.get_extra_data(new_record, items[idx]['snippet']['resourceId']['videoId'])
			db.session.add(new_record)
		
		db.session.commit()