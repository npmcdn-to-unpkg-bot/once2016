from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about', views.about, name='about')
    #url(r'v1/apploint', views.index, name='index'),
]
