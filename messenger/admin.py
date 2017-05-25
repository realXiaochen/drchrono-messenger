from django.contrib import admin

from .models import Messenger
from .forms import MessengerForm

# Register your models here.

class MessengerAdmin(admin.ModelAdmin):
	list_display = ['id',"__unicode__"]
	form = MessengerForm

admin.site.register(Messenger,MessengerAdmin)
