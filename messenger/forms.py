from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Messenger

class MessengerForm(forms.ModelForm):

	class Meta:
		model = Messenger
		fields = ['name']
		start_date = forms.DateField(widget=AdminDateWidget())
		end_date = forms.DateField(widget=AdminDateWidget())