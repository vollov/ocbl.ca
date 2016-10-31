from __future__ import unicode_literals

from django.db import models
from team.models import Team, Player
import uuid
from datetime import datetime
from django.utils.translation import ugettext as _

class Referee(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    name = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    
    def __unicode__(self):
        return '{0} ({1})'.format(self.name, self.city)
    
class Recorder(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    name = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    
    def __unicode__(self):
        return '{0} ({1})'.format(self.name, self.city)
    
class Timer(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    name = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    
    def __unicode__(self):
        return '{0} ({1})'.format(self.name, self.city)
    
class Season(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    name = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    year = models.CharField(max_length=4, blank=False, null=False)

    def __unicode__(self):
        return self.name
    
from content.models import Album

class Game(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    season = models.ForeignKey(Season)
    host = models.ForeignKey(Team,related_name='+')
    guest = models.ForeignKey(Team, related_name='+')
    host_score = models.IntegerField(default=0, blank=True, null=True)
    guest_score = models.IntegerField(default=0, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    finished = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable = True)
    master_referee = models.ForeignKey(Referee, related_name='+', null=True)
    secondary_referee = models.ForeignKey(Referee, related_name='+', null=True)
    recorder=models.ForeignKey(Recorder, null=True)
    timer= models.ForeignKey(Timer, null=True)
    
    album = models.ForeignKey(Album, null=True)
    
    def __unicode__(self):
        return '{0} {1} vs {2}'.format(self.season.year, self.host.name,self.guest.name)

    def name(self):
        return '{0} vs {1}'.format(self.host.name,self.guest.name)
    
class Start_Status:
    STARTER = 'Y'
    SUBSTITUTES = 'S'
    NOT_PLAY = 'NP'
    NOT_AVAILABLE = 'NA'
    
    STATUS = (
        (STARTER, _('Starter')),
        (SUBSTITUTES, _('Substitutes')),
        (NOT_PLAY, _('Not Play')),
        (NOT_AVAILABLE, _('N/A')),
    )
    
class PlayerGameScore(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    
    player = models.ForeignKey(Player, null=True, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, null=True, on_delete=models.CASCADE)
    
    starters = models.CharField(max_length=2,
                                      choices=Start_Status.STATUS,
                                      default='NA')
                                      
    personal_foul = models.IntegerField(default=0, blank=True, null=True)
    free_throw = models.IntegerField(default=0)
    field_goal = models.IntegerField(default=0)
    three_point = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True, editable = True)
    
    def total_points(self):
        return self.free_throw + self.field_goal + self.three_point
        
    class Meta:
        db_table = 'palyer_game_score'
        ordering = ['player__number']
