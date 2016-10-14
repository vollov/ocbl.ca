from django.conf.urls import url

from game import views

urlpatterns = [
    url(r'^$', views.games, name='games'),
    #url(r'^player/(?P<user_id>[^/]+)/$', views.player_profile, name='player_profile'),
]
