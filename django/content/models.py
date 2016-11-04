from __future__ import unicode_literals

from django.db import models
from app import settings

import uuid, os, logging
logger = logging.getLogger(__name__)

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
                                      default=settings.LANGUAGE_CODE)
    page = models.ForeignKey('Page', null=True)
    
    def __unicode__(self):
        return self.code

#######################################################################
# system settings
#######################################################################

class DataType:
    STRING = 's'
    NUMBER = 'n'
    BOOLEAN = 'b'
    
    TYPES = (
        (STRING, 'string'),
        (NUMBER, 'number'),
        (BOOLEAN, 'boolean'),
    )
    
class SystemSetting(models.Model):
    DATATYPE_CHOICES = DataType.TYPES
    
    name = models.CharField(max_length=32, blank=True, null=True)
    value = models.CharField(max_length=32, blank=True, null=True)
    data_type = models.CharField(max_length=2, choices=DATATYPE_CHOICES, default='s')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'system_setting'
        
#######################################################################
# image module
#######################################################################
class Albumn(models.Model):
    """
    container for a set of pictures
    """
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key", default=uuid.uuid4)
    name = models.CharField(max_length=60, db_index=True, unique=True)
    weight = models.IntegerField(default=0)
    slug = models.SlugField(max_length=150, unique=True)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """
        Create a albumn folder in settings.MEDIA_ROOT, before save 
        a new albumn into database.
        """
        logger.debug('albumn model save {0}'.format(__name__))
        
        album_directory = os.path.join(settings.MEDIA_ROOT, self.slug)
        if not os.path.exists(album_directory):
            os.makedirs(album_directory)

        super(Albumn, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return self.name

from storage import OverwriteStorage

def image_upload_path(instance, filename):
    ''' 
    build image upload path
    e.g.
    upload_path = album_slug/f47ac10b-58cc-4372-a567-0e02b2c3d479.jpg
    '''
    file_extension = filename.split('.')[-1]
    saved_name = "{}.{}".format(instance.image_key, file_extension)
    return os.path.join(str(instance.albumn.slug), saved_name)

class Image(models.Model):
    """
    Image objects
    """
    name = models.CharField(max_length=60, blank=True, null=True)
    #f47ac10b-58cc-4372-a567-0e02b2c3d479.jpg
    image_key = models.CharField(max_length=64, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    albumn = models.ForeignKey('Albumn')
    image = models.ImageField(storage=OverwriteStorage(), upload_to=image_upload_path)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    weight = models.IntegerField(default=0)
    
    def image_thumb(self):
        """read only field for display in administration UI"""
        return '<img src="/media/%s" width="100" height="100" />' % (self.image)
     
    image_thumb.allow_tags = True
        
    def __unicode__(self):
        return self.image.name
    
# Handle the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete, pre_save, post_delete
from django.dispatch.dispatcher import receiver

import shutil
@receiver(post_delete, sender=Albumn)
def auto_delete_album_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding Album object is deleted.
    """
    albumn_directory = os.path.join(settings.MEDIA_ROOT, instance.slug)
    if os.path.exists(albumn_directory):
        logger.debug('albumn on delete trigger delete folder {0}'.format(albumn_directory))
        shutil.rmtree(albumn_directory)
    
@receiver(pre_delete, sender=Image)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding Image object is deleted.
    """
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)

@receiver(pre_save, sender=Image)
def auto_delete_image_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding Image object is changed.
    """
    logger.debug('image on delete file {0}'.format(instance.image))
    if not instance.id:
        return False
 
    try:
        old_file = Image.objects.get(pk=instance.id).image
    except Image.DoesNotExist:
        return False
 
    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(False)