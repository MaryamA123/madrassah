from django.conf.urls import url
from . import views
from . import models

urlpatterns = [
    url(r'^$', views.sms, name='sms'), # This is for website.com/sms/
    url(r'houses/', views.houses, name='houses'),
]
