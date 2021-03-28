from django.contrib import admin
from .models import User, Event, EventRequest, Request,Notification

# Register your models here.


class UserAdminSite(admin.ModelAdmin):

	model = User

	fields = ['firstname','lastname','username','email','register_date']

	list_display = ['first_name','last_name','username','email','register_date']






admin.site.register(User,UserAdminSite)
admin.site.register(Event)
admin.site.register(EventRequest)
admin.site.register(Request)
admin.site.register(Notification)

