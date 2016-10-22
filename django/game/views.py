from django.shortcuts import render
from django.utils.translation import ugettext as _

import datetime

from game.models import Season, Game

def games(request):
    """List games for current year"""
    
    time_now = datetime.datetime.now()
    current_year = time_now.year
    
    #season = Entry.objects.all().filter(pub_date__year=2006)
    season = Season.objects.get(year=current_year)
    games = Game.objects.filter(season=season).order_by('start_time','id') 
    
    game_dict = {}
    i = 1
    for game in games:
        g = {}
        g['teams'] = '{0} - {1}'.format(game.host.name, game.guest.name)
        g['address'] = game.address
        g['date'] = game.start_time.strftime('%Y-%m-%d')
        g['time'] = game.start_time.strftime('%H:%M') + ' - ' + game.end_time.strftime('%H:%M')
        if game.finished:
            g['status'] = '{0} - {1}'.format(game.host_score, game.guest_score)
        else:
            g['status'] = _('future_game')
        
        g['master_referee'] = game.master_referee
        g['secondary_referee'] = game.secondary_referee
        g['recorder'] = game.recorder
        g['timer'] = game.timer
        game_dict[i] = g
        i+=1
        
    context = {
        'page_title': _('games'),
        'game_dict':game_dict,
        'season': season.name 
    }
    return render(request,'games.html', context)
