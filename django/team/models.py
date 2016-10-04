from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=64, blank=True, null=True)
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

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
	
	class Meta:
		ordering = ['-pk']
