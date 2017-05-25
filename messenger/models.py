from __future__ import unicode_literals
import datetime, pytz, requests
from django.db import models
from django.conf import settings

# Create your models here.


class Messenger(models.Model):
	token = 1
	name = models.CharField(max_length=20, default = "")

	def __unicode__(self):
		return str(self.name)


def send_emails():

	m = Messenger.objects.first()
	t =  "Bearer " + m.name
	print t
	headers = {
		'Authorization': t,
	}

	# Get all patients
	patients = []

	patients_url = 'https://drchrono.com/api/patients/65140742'
	# while patients_url:
	# rate limit, load one patient here 
	data = requests.get(patients_url, headers=headers)
	data.raise_for_status()
	data = data.json()
	patients.append(data)
		# patients_url = data['next'] # A JSON null on the last page

	res = []
	for p in patients:
		if not p['date_of_birth']:continue
		today = str(datetime.datetime.now()).split(" ")[0]
		#change latter
		if today[5:] != p['date_of_birth'][5:]:
			res.append(p)

	print res
	# Construct the email and send it
	for p in res:
		patient_name =  p['first_name']
		doctor_id =  p['doctor']
		doctor_name = "Dr #" + str(doctor_id)
		to_email_address = p['email']
		from_email_address = 'from@example.com'
		if not to_email_address: continue

		subject = "Happy birthday from Drchrono"
		message = "Hi, " + patient_name + " I'm Dr "+ doctor_name + " from Docchrono Happy birthday!"

		# Logging email information
		print "================================"
		print "Send email from:  " + from_email_address
		print "Send email to:  " + to_email_address
		print "           "+ " Subject:" + subject
		print "           "+ " Content:" + message
		print " "

	# Send Email
		# send_mail(
		# 	subject,
		# 	message',
		# 	'from@example.com',
		# 	[email_address],
		# 	fail_silently=False,
		# 	)
