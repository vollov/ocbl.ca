from django.contrib import admin
from season.models import Season, Session

class SeasonAdmin(admin.ModelAdmin):
    model = Season
    #list_filter = ['year', ]
    list_display = ['name','school','address','year']

class SessionAdmin(admin.ModelAdmin):
    model = Session
    list_filter = ['season', ]
    list_display = ['season','start_time', 'end_time']

admin.site.register(Season, SeasonAdmin)
admin.site.register(Session, SessionAdmin)
