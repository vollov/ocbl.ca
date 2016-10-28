from django.shortcuts import render
from django.utils.translation import ugettext as _

import datetime

from game.models import Season, Game, PlayerGameScore

def game_score(request, game_id):
    """Print score detail"""
    game = Game.objects.get(id = game_id)
    host = game.host
    guest = game.guest
    
    host_scores = PlayerGameScore.objects.filter(game__id = game_id, player__team__id = host.id, )#.order_by(player__number)
        
    guest_scores = PlayerGameScore.objects.filter(game__id = game_id, player__team__id = guest.id)
    
    context = {
        'page_title': _('games'),
        'host_scores':host_scores,
        'guest_scores':guest_scores,
        'host':host,
        'guest':guest,
        'game':game,
    }
    return render(request,'game_score.html', context)
    
    
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
        g['id'] = game.id
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

def game_photo(request, game_id):
    """Display game photoes by game id"""
    
    context = {
        'page_title': _('game_photo'), 
    }
    return render(request,'photos.html', context)

    
def photographs(request):
    """List game photos for season in current year"""
    time_now = datetime.datetime.now()
    current_year = time_now.year
    
    season = Season.objects.get(year=current_year)
    games = Game.objects.filter(season__id = season.id)
    # current_game = games[0]
    # pick up first game in current season
    
    
    context = {
        'page_title': _('photographs'),
        'season': season.name 
    }
    return render(request,'photos.html', context)

