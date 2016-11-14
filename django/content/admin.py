from django.contrib import admin

from models import Block, Page, SystemSetting

class BlockAdmin(admin.ModelAdmin):
    model = Block
    list_filter = ['page', 'locale']
    list_display = ['id','code','locale', 'page']

admin.site.register(Block, BlockAdmin)

class PageAdmin(admin.ModelAdmin):
    model = Page
    
admin.site.register(Page, PageAdmin)

class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ['name','value', 'data_type']

admin.site.register(SystemSetting, SystemSettingAdmin)

from django.utils.text import slugify
from models import Albumn, Image
import logging
logger = logging.getLogger(__name__)

class AlbumnAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'slug','created', 'active']
    prepopulated_fields = {'slug': ('name',)}
    
    def save_model(self, request, obj, form, change):
        '''
        Replace all '-' with '_' in the slug
        ''' 
        logger.debug('albumn admin model save')
        
        obj.slug = slugify(form.cleaned_data['slug'])#.replace('-','_')
        obj.save()

admin.site.register(Albumn, AlbumnAdmin)

class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_thumb',)
    search_fields = ["albumn"]  
    
    
    list_display = ['image_key', 'albumn','name', 'image_thumb', 'created', 'active']
     
admin.site.register(Image, ImageAdmin)