"""ca_website URL Configuration."""

from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from ca_website import settings
from django.conf.urls.static import static
from ca_website.views import HomeView, About, Steps, Meetings, EventInfo, EventDetail, AdditionalResources, test_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', HomeView.as_view(), name='homepage'),
    path('about-ca/', About.as_view(), name='about'),
    path('steps-traditions/', Steps.as_view(), name='steps'),
    path('meeting-schedule/', Meetings.as_view(), name='meetings'),
    path('events/$', EventInfo.as_view(), name='eventinfo'),
    path('events/item/<event-id>', EventDetail.as_view(), name='eventdetail'),
    path('internal-resources', AdditionalResources.as_view(), name='resources'),
    path('test$', test_view, name='homepage'),
    url(r'^$', HomeView.as_view())
]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL,
    #                       document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL)
