"""ca_website URL Configuration."""

from django.urls import path
from django.contrib import admin
from ca_website import settings
from django.conf.urls.static import static
from ca_website.views import EventDetail, AdditionalResources, MeetingDetail
from ca_website.views import HomeView, About, Meetings, EventInfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='homepage'),
    path('about-ca/', About.as_view(), name='about'),
    path('meeting-schedule/', Meetings.as_view(), name='meetings'),
    path('events/', EventInfo.as_view(), name='eventinfo'),
    path('events/item/<event-id>', EventDetail.as_view(), name='eventdetail'),
    path('additional-resources', AdditionalResources.as_view(), name='resources'),
    path('meeting-detail/<pk>/', MeetingDetail.as_view(), name='meetingdetail'),
    path('event-detail/<pk>/', EventDetail.as_view(), name='meetingdetail')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL)
