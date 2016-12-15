from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile

import uuid

class AbstractTeam(models.Model):
	id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
	name = models.CharField(max_length=32, unique=True, blank=True, null=True)
	city = models.CharField(max_length=32, blank=True, null=True)
	captain = models.ForeignKey(User, null=True)
	
	def __unicode__(self):
		return self.name

	class Meta:
		abstract = True


class Team(AbstractTeam):
	active = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True, editable = True)
	
	def save(self):
		team = super(Team, self).save()

class TeamHistory(AbstractTeam):
	team = models.ForeignKey(Team)
	year = models.CharField(max_length=4, blank=False, null=False)
	
	class Meta:
		ordering = ['-pk']

class AbstractPlayer(models.Model):
	id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
	user_profile = models.OneToOneField(UserProfile, null=True)
	#is_captain = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.user_profile.user.username

	def is_captain(self):
		user = self.user_profile.user
		return user.groups.filter(name='captain').exists()
		
	class Meta:
		abstract = True
	
class Player(AbstractPlayer):
	active = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True, editable = True)
	team = models.ForeignKey(Team, null=True)
	number = models.IntegerField(default=0, blank=False, null=False)
	
	def is_captain(self):
		return self.user_profile.user.groups.filter(name='captain').exists()
	
	def is_coach(self):
		return self.user_profile.user.groups.filter(name='coach').exists()
		
	def save(self):
		player = super(Player, self).save()
	
	def full_name(self):
		user = self.user_profile.user
		return user.last_name + ' ' +user.first_name
	
# 	def __unicode__(self):
# 		user = self.user_profile.user
# 		return u''.join((user.last_name,' ',user.first_name )).encode('utf-8').strip()
	
	def __unicode__(self):
		user = self.user_profile.user
		if self.number:
			number = str(self.number)
		else:
			number = 'n/a'
		return user.last_name + ' ' +user.first_name + '(' + number + ') ' + self.team.city
	
	class Meta:
		ordering = ('number',)

class PlayerHistory(AbstractPlayer):
	year = models.CharField(max_length=4, blank=False, null=False)
	team_history = models.ForeignKey(TeamHistory)
	
	class Meta:
		ordering = ['-pk']