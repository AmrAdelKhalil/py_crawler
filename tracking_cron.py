from importers.crawler import *
from config.db import *
from models.videos import *
import urllib2
import os

def load(url, full_path):
	response = urllib2.urlopen(url)	
	fh = open(full_path, 'w')
	fh.write(response.read())
	fh.close()

def get_url_formatted(url):
	return url[url.find('vi')+3:].split('/')
		
def get_video_id(url):
	return url[url.find('v=') + 2:]

def update_data(record, data):
	record.title = data['items'][0]['snippet']['title']
	record.image = data['items'][0]['snippet']['thumbnails']['default']['url']
	record.thumbnail = data['items'][0]['snippet']['thumbnails']['medium']['url']
	record.duration = data['items'][0]['contentDetails']['duration']
	record.views = data['items'][0]['statistics']['viewCount']
	return record

def load_images():

	videos = Videos.query.all()

	for idx in range(len(videos)):
		
		payload = {'part': 'snippet,statistics,contentDetails', 'id': get_video_id(videos[idx].video_url)}
		data = Crawler().get_video_details(payload)
		
		videos[idx] = update_data(videos[idx], data)

		id, img_name = get_url_formatted(videos[idx].thumbnail)
			
		directory_path = 'images/' + id
		
		if not os.path.exists(directory_path):
			os.makedirs(directory_path)
		
		# load thumbnail
		full_path = 'images/' + id + '/' + img_name
		load(videos[idx].thumbnail, full_path)
		videos[idx].downloaded_thumbnail_path = os.getcwd() + full_path

		id, img_name = get_url_formatted(videos[idx].image)

		# load original image
		full_path = 'images/' + id + '/' + img_name
		load(videos[idx].image, full_path)
		videos[idx].downloaded_image_path = os.getcwd() + full_path

	db.session().commit()


		


if __name__ == "__main__":
	load_images()