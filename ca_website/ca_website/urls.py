"""ca_website URL Configuration."""

from django.conf.urls import url
from django.contrib import admin
from ca_website import settings
from django.conf.urls.static import static
from ca_website.views import HomeView, About, Steps, Meetings, EventInfo, EventDetail, AdditionalResources, test_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='homepage'),
    url(r'^about-ca/', About.as_view(), name='about'),
    url(r'^steps-traditions', Steps.as_view(), name='steps'),
    url(r'^meeting-schedule', Meetings.as_view(), name='meetings'),
    url(r'^events$', EventInfo.as_view(), name='eventinfo'),
    url(r'^events/item/(?P<pk>\d+)', EventDetail.as_view(), name='eventdetail'),
    url(r'^internal-resources', AdditionalResources.as_view(), name='resources'),
    url(r'^test$', test_view, name='homepage'),
]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL,
    #                       document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL)
