from __future__ import unicode_literals

from datetime import date
from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #phone = models.CharField(max_length=64, blank=False, null=False)
    #birthday = models.DateField(blank=False, null=False)
    birth_year = models.IntegerField(default=1988, blank=False, null=False)
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)

#     height = models.IntegerField(default=0, blank=False, null=False)
    
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        user = self.user
        return user.last_name + ' ' +user.first_name

    
    def age(self):
        current_year = date.today().year
        return current_year - self.birth_year
        
#     def age(self):
#         birthday = self.birthday
#         today = date.today()
#         return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        
