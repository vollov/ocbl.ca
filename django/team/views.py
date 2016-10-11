from django.contrib.auth.decorators import login_required
from __builtin__ import False
import logging
logger = logging.getLogger(__name__)

from team.forms import EnrollForm
from team.models import Player
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404
from accounts.models import UserProfile

@login_required
def player_enroll(request, user_id):
    """HTTP GET to show player enroll form"""
    user = User.objects.get(id = user_id)
    enroll_form = EnrollForm()
         
    context = {
        'page_title': 'Enroll a Team',
        'user': user,
        'enroll_form': enroll_form,
    }
    return render(request,'player_enroll.html', context)

@login_required    
def post_enroll(request):
    """Process HTTP POST for player enroll"""
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
def player_profile(request, user_id):
    """player profile - HTTP GET /team/player/@id"""

    player = Player.objects.get(user_profile__user__id = user_id)
    context = {'page_title':'player profile', 
                   'player': player,
                   'user_profile': player.user_profile}
    
    return render(request, 'player_profile.html', context)

@login_required
def captain_profile(request, user_id):
    """captain profile - HTTP GET /team/captain/@id"""

    captain = Player.objects.get(user_profile__user__id=user_id)
    context = {'page_title':'player profile', 
                   'captain': captain,
                   'user_profile': captain.user_profile}
    
    return render(request, 'captain_profile.html', context)

class ProfileService:
    """
    Service class to manage player status 
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
        
            
    
            

