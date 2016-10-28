from django.conf.urls import url

from game import views

urlpatterns = [
    url(r'^$', views.games, name='games'),
    url(r'^(?P<game_id>[^/]+)/$', views.game_score, name='game_score'),
    url(r'^(?P<game_id>[^/]+)/photo$', views.game_score, name='game_photos'),
]
