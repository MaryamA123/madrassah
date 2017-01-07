from django.conf.urls import url
from . import views
from . import models
from views import StudentList

urlpatterns = [
    url(r'^$', views.sms, name='sms'), # This is for website.com/sms/
    url(r'houses/', views.houses, name='houses'),
    url(r'^students/$', StudentList.as_view()),
]
