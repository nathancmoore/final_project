"""ca_website URL Configuration."""

from django.conf.urls import url
from django.contrib import admin
from ca_website import views, settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.home_view, name='homepage'),
    # url(r'^about-ca/',),
    # url(r'^steps-traditions', ),
    # url(r'^meeting-schedule', ),
    # url(r'^events$', ),
    # url(r'^events/item/(?P<pk>\d+)', ),
    # url(r'^internal-resources', ),
]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL,
    #                       document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL)
