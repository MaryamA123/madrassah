from django.conf.urls import url
from . import views
from . import models

urlpatterns = [
    url(r'^$', views.sms, name='sms'), # This is for website.com/sms/
    url(r'houses/', views.houses),
    url(r'^(?P<house_id>[0-9]+)/$', views.housesGroup)
]
