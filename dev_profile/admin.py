from django.contrib import admin

# Register your models here.
from .models import *

class WebsiteInfoAdmin(admin.ModelAdmin):
	fieldsets = [
		('Page Information', {'fields' : ['page_name', 'page_owner', 'page_info', 'page_photo']}),
		('Page Quote', {'fields' : ['page_message', 'page_message_author'], 'classes' : ['collapse']}),		
	]

	list_display = ('page_owner', 'page_info')

	def has_add_permission(self, request):
		count = WebsiteInfo.objects.all().count()
		if not count:
			return True
		return False


#Admin class registrations

admin.site.register(WebsiteInfo, WebsiteInfoAdmin)