from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.db.models import Avg, Sum

import datetime

from models import Season, Game, PlayerGameScore
from team.models import Player
from service import GamePhotoHelper
from content.models import Image

import logging
logger = logging.getLogger(__name__)

def game_score(request, game_id):
    """Print score detail"""
    logger.debug('calling game_score with game_id={0}', game_id)
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
    
def season_stat(request, year):
    """
    Listing players by ranking
          <th>#</th>
          <th>Player</th>
          <th>Number</th>
          <th>Team</th>
          <th>personal foul</th>
          <th>free throw</th>
          <th>field goal</th>
          <th>three_point</th>
          <th>total_points</th>
          
    personal_foul = models.IntegerField(default=0, blank=True, null=True)
    free_throw = models.IntegerField(default=0)
    field_goal = models.IntegerField(default=0)
    three_point = models.IntegerField(default=0)
    """
    season = Season.objects.get(year=year)
    scores = PlayerGameScore.objects.filter(game__season__id=season.id).values('player').annotate(
                                    personal_foul_sum=Sum('personal_foul'),
                                    free_throw_sum=Sum('free_throw'),
                                    field_goal_sum=Sum('field_goal'),
                                    three_point_sum=Sum('three_point'),)
    
    stat_list = []
    
    for score in scores:
        s = {}
        player_id = score['player']

        player = Player.objects.get(id=player_id)
        s['player'] = player.full_name
        s['number'] = player.number
        s['team'] = player.team.name
        s['personal_foul_sum'] = score['personal_foul_sum']
        s['free_throw_sum'] = score['free_throw_sum']
        s['field_goal_sum'] = score['field_goal_sum']
        s['three_point_sum'] = score['three_point_sum']
        s['total_point_sum'] = score['free_throw_sum'] + score['field_goal_sum'] + score['three_point_sum']
    
        stat_list.append(s)
        
        stat_list.sort(key=lambda x: x['total_point_sum'], reverse=True)
        
    #print scores.query.__str__()
    context = {
        'page_title': _('stats'),
        'stat_list':stat_list,
    }
    return render(request,'season_stats.html', context)
    
    
    
def games_by_year(request, year):
    
    seasons = Season.objects.all()
    
    season = Season.objects.get(year=year)
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
        'season': season,
        'seasons':seasons
    }
    return render(request,'games.html', context)
    
    
def games(request):
    """List games for current year"""
    
    time_now = datetime.datetime.now()
    current_year = time_now.year
    
    return games_by_year(request, current_year)
    #season = Entry.objects.all().filter(pub_date__year=2006)
    

def game_photo(request, albumn_slug):
    """Display game photoes by game id"""
    
    time_now = datetime.datetime.now()
    current_year = time_now.year
    
    season = Season.objects.get(year=current_year)
    games = Game.objects.filter(season__id = season.id).exclude(albumn__isnull=True)
    
    game = Game.objects.get(albumn__slug=albumn_slug)
    
    # You cannot query against model methods or properties.
#     thumbnails = game.albumn.image_set.filter(is_thumbnail=True)
#     if thumbnails:
#         game.thumbnail = thumbnails[0]
#     else:
#         game.thumbnail = 'na.jpg'
    
    photos = GamePhotoHelper.get_photos(albumn_slug)
    
    context = {
        'page_title': _('game_photo'),
        'game_dict': GamePhotoHelper.get_games(games),
        'photos':photos,
        'albumn_slug':albumn_slug,
        'season': season.name,
    }
    return render(request,'photos.html', context)

    
def photographs(request):
    """List game photos for season in current year"""
    time_now = datetime.datetime.now()
    current_year = time_now.year
    
    season = Season.objects.get(year=current_year)
    # filter out albumn with no photos
    games = Game.objects.filter(season__id = season.id).exclude(albumn__isnull=True)
    if games: 
        game_dict = GamePhotoHelper.get_games(games)
        current_game = games[0]
        # pick up first game in current season
        photos = GamePhotoHelper.get_photos(current_game.albumn.slug)
    else:
        # do empty view
        game_dict = {}
        photos = []
        
    context = {
        'page_title': _('photographs'),
        'game_dict': game_dict,
        'photos': photos,
        'season': season.name,
    }
    return render(request,'photos.html', context)

