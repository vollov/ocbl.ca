from django.conf.urls import url

from game import views

urlpatterns = [
    url(r'^$', views.games, name='games'),
    url(r'^photos/$', views.photographs, name='photographs'),
    url(r'^score/(?P<game_id>[^/]+)/$', views.game_score, name='game_score'),
    url(r'^(?P<albumn_slug>[^/]+)/photo/$', views.game_photo, name='game_photo'),
    
]
