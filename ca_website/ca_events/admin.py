from django.contrib import admin

# Register your models here.
from ca_events.models import Meeting, ServiceMeeting, Events
admin.site.register(Meeting)
admin.site.register(ServiceMeeting)
admin.site.register(Events)