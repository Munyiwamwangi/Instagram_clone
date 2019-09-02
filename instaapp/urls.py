from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'posts/$', views.welcome, name='welcome'),
    url(r'^search/', views.search_image, name='search_image'),
    url(r'^accunts/profile/$', views.edit_profile_info, name='edit_profile_info'),
    url(r'^upload/$', views.Photo, name='uploadPhoto'),
    url(r'comment/(\d+)', views.comment, name='comment'),
    url(r'^profile_info/$', views.profile, name='profile_info'),

    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',
    #     views.past_days_images, name='pastImages'),
    # url(r'^search/', views.search_results, name='search_results'),
]

#To serve uploaded images on the development server we need to configure our urls.py to register the MEDIA_ROOT route.
# add to the urlpatterns images static route that references the location to the uploaded files.

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
