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
		
def load_images():

	videos = Videos.query.filter(Videos.downloaded_thumbnail_path == '', Videos.downloaded_image_path == '').all()

	for idx in range(len(videos)):
		
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