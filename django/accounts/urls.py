from django.conf.urls import url

from views import register, user_login, user_logout
from content.service import SettingService

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', user_login, name='user_login'),
    url(r'^logout/$', user_logout, name='logout'),
]
