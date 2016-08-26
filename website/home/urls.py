from django.conf.urls import url
from . import views

from django.conf import settings

# Refer to https://docs.djangoproject.com/en/1.10/intro/tutorial03/
app_name = "home"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^public_photos/$', views.public_photos, name='public_photos'),
    url(r'^user_photo/$', views.user_photo, name='user_photo'),
    url(r'^user_photo/result/$', views.user_photo_result, name='user_photo_result'),
    url(r'^appointment/$', views.appointment, name='appointment'),
    url(r'^appointment/result/$', views.appointment_result, name='appointment_result'),
    # Admin url
    url(r'^once/$', views.once_manage, name='once_manage'),

    url(r'^wxpay/$', views.pay, name='pay'),
    url(r'^paydetail/$', views.paydetail, name='paydetail'),
    url(r'^payback/$', views.payback, name='payback'),
]
