from __builtin__ import False
import logging
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from accounts.models import UserProfile
from team.forms import EnrollForm, PlayerForm
from team.models import Player, Team

logger = logging.getLogger(__name__)

def team_detail(request, team_id):
    """Show players and captains by team id, show game results
     - HTTP GET /team/@team_id"""
    teams = Team.objects.filter(active=True).order_by('name','id')
    current_team = Team.objects.get(id=team_id)
    teamHelper = TeamHelper()
    # all active players
    players = Player.objects.filter(team=current_team, active=True).order_by('id')
    
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
    logger.debug('calling player enroll with user_id={0}'.format(user_id))
    user = User.objects.get(id = user_id)
    enroll_form = EnrollForm()
         
    context = {
        'page_title': 'Enroll a Team',
        'user': user,
        'enroll_form': enroll_form,
    }
    return render(request,'player_enroll.html', context)

@login_required
def player_number(request, team_id,player_id):
    """HTTP GET to show player enroll form
    Role = [player]
    """
    logger.debug('calling player number with player_id={0}'.format(player_id))
    player_form = PlayerForm(data=request.POST)
    if player_form.is_valid():
        player_data = player_form.save(commit=False)
        logger.debug('get player number={0}'.format(player_data.number))
        player=Player.objects.get(id=player_id)
        player.number = player_data.number
        player.save()
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

    player = Player.objects.get(id = player_id)
    player.active = True
    player.save()
    
    return HttpResponseRedirect('/team/{0}/manage'.format(player.team.id))
    
@login_required
def player_profile(request, user_id):
    """player profile - HTTP GET /team/player/@id
    Role = [player]
    """

    player = Player.objects.get(user_profile__user__id = user_id)
    context = {'page_title':'player profile', 
                   'player': player,
                   'user_profile': player.user_profile}
    
    return render(request, 'player_profile.html', context)

@login_required
def captain_profile(request, user_id):
    """captain profile - HTTP GET /team/captain/@id
    Role = [captain]
    """

    captain = Player.objects.get(user_profile__user__id=user_id)
    context = {'page_title':'player profile', 
                   'captain': captain,
                   'user_profile': captain.user_profile}
    
    return render(request, 'captain_profile.html', context)

@login_required
def team_manage(request, team_id):
    """captain profile - HTTP GET /team/@team_id/manage
    Role = [captain]
    """
    user_id = request.session['user_id']
    current_team = Team.objects.get(id=team_id)
    teamHelper = TeamHelper()
    
    player_form = PlayerForm()
    # get all players
    players = Player.objects.filter(team=current_team).order_by('id')
    
    context = {'page_title':'Team {0}'.format(current_team.name),
               'user_id':user_id,
               'team_id':team_id,
               'player_form':player_form,
                   'players_dict':teamHelper.get_players_for_view(players)}
    
    return render(request, 'team_manage.html', context)

class TeamHelper:
    
    def __init__(self):
        pass
    
    def get_players_for_view(self, players):
        
    
        players_dict = {}
        i = 1
        for player in players:
            p = {}
            user = player.user_profile.user
            first_name = unicode(user.first_name)
            last_name = unicode(user.last_name)
            if player.is_captain():
                p['name'] = u''.join((last_name,first_name,'(',_('captain'),')')).encode('utf-8').strip()
            else:
                p['name'] = u''.join((last_name,first_name )).encode('utf-8').strip()
            p['id'] = player.id
            p['age'] = player.user_profile.age()
            p['active'] = player.active
            if not player.number:
                p['number'] = 'n/a'
            else:
                p['number'] = player.number
                
            players_dict[i] = p
            i+=1
        return players_dict

class ProfileService:
    """
    Service class to manage player status
    Role = [all] 
    """
    def __init__(self, user_id):
        self.user_id = user_id
        
    def getProfile(self):
        """direct profile view for players and captains"""
        
        if self.is_approved_player():
            logger.debug('approved player {0}'.format(self.user_id))
            if self.is_captain():
                return '/team/captain/{0}'.format(self.user_id)
                #return captain_profile(request)
            else:
                return '/team/player/{0}'.format(self.user_id)
                #return player_profile(request)
        else:
            logger.debug('ProfileService=> /team/player/{0}/enroll'.format(self.user_id))
            return '/team/player/{0}/enroll'.format(self.user_id)
            #return player_enroll(request)
        
    def is_captain(self):
        """ check if the user is a captain"""
        if self.is_approved_player():
            player = Player.objects.get(user_profile__user__id = self.user_id)
            if player.is_captain():
                return True
            else:
                return False
        else:
            return False
        
    def is_approved_player(self):
        """ check if the player is approved by captain"""
        if Player.objects.filter(user_profile__user__id = self.user_id, active=True).exists():
            return True
        else:
            return False

