from __future__ import unicode_literals

from django.db import models
from datetime import date

import uuid

from team.models import Team

class Season(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    team = models.ForeignKey(Team)
    name = models.CharField(max_length=64, blank=True, null=True)
    school = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    
    class Meta:
        db_table = 'season'
        ordering = ['-start_date']
        
    def __unicode__(self):
        return self.name
    
    def is_current(self):
        current_date = date.today()
        if current_date >= self.start_date and current_date <= self.end_date:
            return True
        else:
            return False
        
    def year(self):
        return self.start_date.strftime('%Y')

class Session(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    season = models.ForeignKey(Season, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'session'
        ordering = ['start_time']
        
    def __unicode__(self):
        return 'Session'

    def week_day(self):
        return self.start_time.strftime('%a')
    
    def date(self):
        # '%Y-%m-%d %H:%M'
        return self.start_time.strftime('%Y-%m-%d')
