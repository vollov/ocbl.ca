from django.contrib import admin

from models import Block, Page

class BlockAdmin(admin.ModelAdmin):
    model = Block
    list_filter = ['page', 'locale']
    list_display = ['id','code','locale', 'page']

class PageAdmin(admin.ModelAdmin):
    model = Page
    
admin.site.register(Block, BlockAdmin)
admin.site.register(Page, PageAdmin)