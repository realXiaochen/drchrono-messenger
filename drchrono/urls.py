from django.conf.urls import include, url
from django.views.generic import TemplateView
import datetime, pytz, requests

from .views import page


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    url(r'', include('social.apps.django_app.urls', namespace='social')),

    url(r'^accounts/profile/', page, name="login")

]




