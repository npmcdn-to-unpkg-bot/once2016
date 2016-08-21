from django.conf.urls import url
from . import views

# Refer to https://docs.djangoproject.com/en/1.10/intro/tutorial03/
app_name = "home"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^photos/$', views.photos, name='photos'),
    url(r'^getphoto/$', views.getphoto, name='getphoto'),
    url(r'^(?P<question_id>[0-9]+)/action/$', views.getphoto_action, name='getphoto_action'),
    url(r'^(?P<question_id>[0-9]+)/result/$', views.getphoto_result, name='getphoto_result'),
]
