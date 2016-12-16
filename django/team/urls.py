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
    
    # ================================================
    # public views for a team
    # ================================================
    url(r'^$', views.teams, name='teams'),
    url(r'^(?P<name>[^/]+)$', views.team_detail, name='team_detail'),
    
    # ================================================
    # profile self management
    #    player_profile     - player/(?P<username>
    #    captain_profile    - captain/(?P<username>
    #    player_edit
    # ================================================
    
    # show player profile in edit form
    url(r'^player/(?P<username>[^/]+)/$', views.player_profile, name='player_profile'),
    
    # show captain profile in edit form
    url(r'^captain/(?P<username>[^/]+)/$', views.captain_profile, name='captain_profile'),
    
    # show 
    url(r'^player/(?P<username>[^/]+)/edit$', views.player_edit, name='player_edit'),
    url(r'^player/(?P<username>[^/]+)/enroll$', views.player_enroll, name='player_enroll'),
    url(r'^(?P<team_id>[^/]+)/player/(?P<username>[^/]+)/number$', views.player_number, name='player_number'),
    url(r'^enroll/$', views.post_enroll, name='post_enroll'),
    
    # ================================================
    # player status update
    #    (F)free    - player can join other teams
    #    (P)pending - player left the league, or new apply to join
    #    (A)active  - player is active
    # ================================================
    
#     # approve a player, player became active, link to a team
#     url(r'^player/(?P<player_id>[^/]+)/join$', views.player_join, name='player_join'),
#     
#     # make a player free
#     url(r'^player/(?P<player_id>[^/]+)/free$', views.player_free, name='player_free'),
#     
#     # make a player to pending in a team
#     url(r'^player/(?P<player_id>[^/]+)/deactive$', views.player_deactive, name='player_deactive'),
#     
#     
    # ================================================
    # players lists - current, pending, search
    # ================================================
    
    # current-players for editing
    url(r'^players/(?P<name>[^/]+)/current$', views.team_current_players, name='team_current_players'),
     
    # pending-players, players requested to join
    #url(r'^players/(?P<name>[^/]+)/pending$', views.team_pending_players, name='team_pending_players'),
    

    
    
#    url(r'^profile/$', views.profile, name='profile'),
#     url(r'^logout/$', views.user_logout, name='logout'),
]
