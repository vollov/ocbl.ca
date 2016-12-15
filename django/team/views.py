from __builtin__ import False

from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from accounts.models import UserProfile
from team.forms import EnrollForm, PlayerForm
from team.models import Player, Team
from service import TeamHelper

import logging
logger = logging.getLogger(__name__)

def team_detail(request, name):
    """Show players and captains by team id, show game results
     - HTTP GET /team/@team_name"""
    teams = Team.objects.filter(active=True).order_by('name','id')
    current_team = Team.objects.get(name=name)
    teamHelper = TeamHelper()
    # all active players
    players = Player.objects.filter(team=current_team, active=True).order_by('number')

    context = {
        'page_title': current_team,
        'teams':teams,
        'current_team':current_team,
        'players_dict':teamHelper.get_players_for_view(players)
    }
    return render(request,'teams.html', context)

def teams(request):
    """list all teams"""
    
    teams = Team.objects.filter(active=True).order_by('name','id')
    
    current_team = teams[0]
    teamHelper = TeamHelper()
    players = Player.objects.filter(team=current_team, active=True).order_by('id')
    
    context = {
        'page_title': _('teams'),
        'teams':teams,
        'current_team':current_team,
        'players_dict':teamHelper.get_players_for_view(players)
    }
    return render(request,'teams.html', context)


@login_required
def player_enroll(request, user_id):
    """HTTP GET to show player enroll form
    Role = [player]
    """
    if request.user.id != long(user_id):
        raise PermissionDenied
    
    user = User.objects.get(id = user_id)
    enroll_form = EnrollForm()
    
    context = {
        'page_title': 'Enroll a Team',
        'user': user,
        'enroll_form': enroll_form,
    }
    return render(request,'player_enroll.html', context)

@login_required
def player_number(request, team_id, player_id):
    """HTTP GET to show player enroll form
    Role = [player]
    """
    #only captain can change player number
    # only captain can approve player
    if not request.user.groups.filter(name='captain').exists():
        raise PermissionDenied
    
    player = Player.objects.get(id = player_id)
    current_user_id=request.user.id
    current_user = Player.objects.get(user_profile__user__id = current_user_id)
    
    # captain can only approve players, who in his team
    if current_user.team.id != player.team.id:
        raise PermissionDenied
    
    player_form = PlayerForm(data=request.POST)
    if player_form.is_valid():
        player_data = player_form.save(commit=False)
        logger.debug('get player number={0}'.format(player_data.number))
        
        player.number = player_data.number
        player.save()
        
        logger.info('calling player id={0} changed to number {1}'.format(player.user_profile.user.username, player_data.number))
        
    return HttpResponseRedirect('/team/{0}/manage'.format(team_id))       

@login_required    
def post_enroll(request):
    """Process HTTP POST for player enroll
    Role = [player]
    """
    user_id = request.session['user_id']
    user_profile = UserProfile.objects.get(user__id = user_id)
    
    enroll_form = EnrollForm(data=request.POST)
    
    if enroll_form.is_valid():
        
        player = enroll_form.save(commit=False)
        team = enroll_form.cleaned_data['team']

        # set the user
        if Player.objects.filter(user_profile__user__id = user_id).exists():
            if team.id != player.team.id:
                player = Player.objects.get(user_profile__user__id = user_id)
                player.active = False
        
        player.user_profile = user_profile
        player.team = team        
        player.save()
        
        logger.info('player {0} applied enroll'.format(user_profile.user.username))
        
        context = {'page_title':'team detail', 
                   'team_name': team.name}
        return render(request, 'enroll_submitted.html', context)
    else:
        print enroll_form.errors
        raise Http404("your enrollment failed.")
        
@login_required
def player_approve(request, player_id):
    """captain approve a player to join a team, by setting the player to active. 
    - HTTP GET /team/player/@player_id/approve
    - Role = [captain]
    """
    
    # only captain can approve player
    if not request.user.groups.filter(name='captain').exists():
        raise PermissionDenied
    
    player = Player.objects.get(id = player_id)
    current_user_id=request.user.id
    current_user = Player.objects.get(user_profile__user__id = current_user_id)
    
    # captain can only approve players, who in his team
    if current_user.team.id != player.team.id:
        raise PermissionDenied
    
    player.active = True
    player.save()
    
    logger.info('captain approved player {0}'.format(player.user_profile.user.username))
    
    return HttpResponseRedirect('/team/{0}/manage'.format(player.team.id))
    
@login_required
def player_profile(request, user_id):
    """player profile - HTTP GET /team/player/@id
    Role = [player]
    """

    if request.user.id != long(user_id):
        raise PermissionDenied
    
    player = Player.objects.get(user_profile__user__id = user_id)
    context = {'page_title':'player profile', 
                   'player': player,
                   'user_profile': player.user_profile}
    
    return render(request, 'player_profile.html', context)

@login_required
def captain_profile(request, user_id):
    """captain profile - HTTP GET /team/captain/@user_id
    Role = [captain]
    
    only show team that this captain is belongs to 
    """
    if request.user.id != long(user_id):
        raise PermissionDenied
    logger.debug('request.user={0}, user={1}'.format(type(request.user.id), type(user_id)))

    captain = Player.objects.get(user_profile__user__id=user_id)
    context = {'page_title':'player profile', 
                   'captain': captain,
                   'user_profile': captain.user_profile}
    
    return render(request, 'captain_profile.html', context)

@login_required
def player_edit(request, user_id):
    pass
    
@login_required
def team_players_edit(request, name):
    """captain profile - HTTP GET /team/@team_name/manage
    Role = [captain]
    
    only show team that this captain is belongs to
    """
    
    user_id = request.session['user_id']
    captain = Player.objects.get(user_profile__user__id=user_id)

    if captain.team.name != name:
        raise PermissionDenied
    
    current_team = Team.objects.get(name=name)
    teamHelper = TeamHelper()
    
    player_form = PlayerForm()
    # get all players
    players = Player.objects.filter(team=current_team).order_by('id')
    
    context = {'page_title':'Team {0}'.format(current_team.name),
               'user_id':user_id,
               'team_name': name,
               'view_name' : 'team_players_edit',
               'player_form':player_form,
                   'players_dict':teamHelper.get_players_for_view(players)}
    
    return render(request, 'team_players_edit.html', context)



