from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
import time
from messenger.models import send_emails


@task(name="main_task")
def simple_task():
	# t = 60*60*24
	t = 15
	while True:
		send_emails()
		time.sleep(t)
		print 'Wait for ' + str(t) + ' s'
