from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'v1/apploint', views.index, name='index'),
]
