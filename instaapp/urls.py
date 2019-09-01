from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'', views.home, name="home"),
    url(r'^about/$', views.about, name='about'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',
    #     views.past_days_images, name='pastImages'),
    url(r'^search/', views.search_results, name='search_results'),
]

#To serve uploaded images on the development server we need to configure our urls.py to register the MEDIA_ROOT route.
# add to the urlpatterns images static route that references the location to the uploaded files.

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
