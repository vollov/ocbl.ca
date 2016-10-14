from django.conf.urls import url

from team import views

urlpatterns = [
    url(r'^$', views.teams, name='teams'),
    url(r'^enroll/$', views.post_enroll, name='post_enroll'),
    url(r'^(?P<team_id>[^/]+)$', views.team_detail, name='team_detail'),
    url(r'^player/(?P<user_id>[^/]+)/$', views.player_profile, name='player_profile'),
    url(r'^player/(?P<user_id>[^/]+)/enroll$', views.player_enroll, name='player_enroll'),
    url(r'^player/(?P<player_id>[^/]+)/approve$', views.player_approve, name='player_approve'),
    url(r'^captain/(?P<user_id>[^/]+)/$', views.captain_profile, name='captain_profile'),
    
    url(r'^(?P<team_id>[^/]+)/manage$', views.team_manage, name='team_manage'),
#    url(r'^profile/$', views.profile, name='profile'),
#     url(r'^logout/$', views.user_logout, name='logout'),
]
