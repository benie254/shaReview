from django.urls import path,re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.new_project,name='new-project'),
    url(r'^accounts/profile/(\d+)/$',views.profile,name='profile'),
    url(r'^profile/(\d+)/bio/add-update/$',views.bio,name='bio'),
    path('add/project/',views.new_project,name='new-project')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
