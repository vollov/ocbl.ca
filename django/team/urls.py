from django.conf.urls import url

from team import views

"""
URL Map

/team_id/players      [manage player number, active]
/team_id/events       [team internal meetings]
/team_id/upload       [upload team picture]
/team_id/photos       [team photos]
/team_id/finance      [team expenses]
/team_name/schedules    [team training session schedule]
/team_name/school 

[schedule]
1) season
team_id
name
school
start_date
end_date
address

2) session
start_time
end_time

"""

urlpatterns = [
    url(r'^$', views.teams, name='teams'),
    url(r'^enroll/$', views.post_enroll, name='post_enroll'),
    url(r'^(?P<team_id>[^/]+)$', views.team_detail, name='team_detail'),
    url(r'^player/(?P<user_id>[^/]+)/$', views.player_profile, name='player_profile'),
    url(r'^player/(?P<user_id>[^/]+)/edit$', views.player_edit, name='player_edit'),
    url(r'^player/(?P<user_id>[^/]+)/enroll$', views.player_enroll, name='player_enroll'),
    url(r'^(?P<team_id>[^/]+)/player/(?P<player_id>[^/]+)/number$', views.player_number, name='player_number'),
    url(r'^player/(?P<player_id>[^/]+)/approve$', views.player_approve, name='player_approve'),
    url(r'^captain/(?P<user_id>[^/]+)/$', views.captain_profile, name='captain_profile'),
    
    url(r'^(?P<team_id>[^/]+)/manage$', views.team_manage, name='team_manage'),
#    url(r'^profile/$', views.profile, name='profile'),
#     url(r'^logout/$', views.user_logout, name='logout'),
]
