from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile

import uuid

class AbstractTeam(models.Model):
	id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
	name = models.CharField(max_length=32, blank=True, null=True)
	city = models.CharField(max_length=32, blank=True, null=True)

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
	captain = models.ForeignKey(User, null=True)
	class Meta:
		ordering = ['-pk']

class AbstractPlayer(models.Model):
	id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
	user_profile = models.OneToOneField(UserProfile, null=True)
	#is_captain = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.user_profile.user.username

	class Meta:
		abstract = True
	
class Player(AbstractPlayer):
	active = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True, editable = True)
	team = models.ForeignKey(Team, null=True)
	
	def is_captain(self):
		return self.user_profile.user.groups.filter(name='captain').exists()
       
	def save(self):
		player = super(Player, self).save()
	
class PlayerHistory(AbstractTeam):
	year = models.CharField(max_length=4, blank=False, null=False)
	team_history = models.ForeignKey(TeamHistory)
	
	class Meta:
		ordering = ['-pk']