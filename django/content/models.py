from __future__ import unicode_literals

from django.db import models
from app.settings import LANGUAGE_CODE

import uuid

class Language:
    ENGLISH = 'en'
    CHINESE = 'zh'
    
    LANGUAGES = (
        (ENGLISH, 'English'),
        (CHINESE, 'Chinese'),
    )
    
class Page(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    name = models.CharField(max_length=32, unique=True, blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
class Block(models.Model):
    LANGUAGE_CHOICE = Language.LANGUAGES
    
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    code = models.CharField(max_length=64, unique=True, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    locale = models.CharField(max_length=2,
                                      choices=LANGUAGE_CHOICE,
                                      default=LANGUAGE_CODE)
    page = models.ForeignKey('Page', null=True)
    
    def __unicode__(self):
        return self.code
