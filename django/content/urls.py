from django.conf.urls import url

from content import views

urlpatterns = [

    url(r'^upload/$', views.upload_photo, name='upload_photo'),
#     url(r'^logout/$', views.user_logout, name='logout'),
]
