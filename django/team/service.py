
from django.utils.translation import ugettext as _

import logging
logger = logging.getLogger(__name__)

from team.models import Player, Team

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
            #logger.debug('helper user={0}'.format(player.number))
            if player.is_captain():
                p['name'] = u''.join((last_name,first_name,'(',_('captain'),')')).encode('utf-8').strip()
            elif player.is_coach():
                p['name'] = u''.join((last_name,first_name,'(',_('coach'),')')).encode('utf-8').strip()
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