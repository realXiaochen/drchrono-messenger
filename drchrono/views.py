import datetime, pytz, requests
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from messenger.models import send_emails
from .tasks import simple_task

def page(request):

# 	send_emails()
	simple_task.delay()
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

# 		# send_mail(
# 		# 	subject,
# 		# 	message',
# 		# 	'from@example.com',
# 		# 	[email_address],
# 		# 	fail_silently=False,
# 		# 	)









