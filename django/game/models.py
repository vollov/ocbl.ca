from __future__ import unicode_literals

from django.db import models
from team.models import Team
import uuid

class Referee(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    name = models.CharField(max_length=64, blank=True, null=True)

    def __unicode__(self):
        return self.name
    
class Season(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    name = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    year = models.CharField(max_length=4, blank=False, null=False)

    def __unicode__(self):
        return self.name
    
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
    referee = models.ForeignKey(Referee, null=True)
    def __unicode__(self):
        return '{0} vs {1}'.format(self.host.name,self.guest.name)
