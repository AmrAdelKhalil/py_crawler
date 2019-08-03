import os
from crontab import CronTab

def image_cron():
	my_cron = CronTab(user='amradel')
	job = my_cron.new(command='cd ' +  os.getcwd() + ' && /usr/bin/python2.7 image_downloader.py')
	job.minute.every(59)
	my_cron.write()


def tracking_cron():
	my_cron = CronTab(user='amradel')
	job = my_cron.new(command='cd ' +  os.getcwd() + ' && /usr/bin/python2.7 tracking_cron.py')
	job.dow.on('SUN')
	my_cron.write()

def run_cron():
	image_cron()
	tracking_cron()