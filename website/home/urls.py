from django.conf.urls import url
from . import views

# Refer to https://docs.djangoproject.com/en/1.10/intro/tutorial03/
app_name = "home"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^photos/$', views.photos, name='photos'),
    url(r'^getphoto/$', views.getphoto, name='getphoto'),
    url(r'^getphoto/result/$', views.getphoto_result, name='getphoto_result'),
    url(r'^appointment/$', views.appointment, name='appointment'),
    url(r'^appointment/result/$', views.appointment_result, name='appointment_result'),
    # Admin url
    url(r'^once/$', views.once_manage, name='once_manage'),
]
