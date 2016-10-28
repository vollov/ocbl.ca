class GamePhotoHelper:
    """Helper classs to prepare Game photo view data"""
    def __init__(self):
        pass
    
    def get_game_photo_for_view(self, games):
        
        game_dict = {}
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