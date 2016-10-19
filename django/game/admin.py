from django.contrib import admin

from game.models import Season, Game, Referee

class SeasonAdmin(admin.ModelAdmin):
    model = Season
    list_filter = ['year', ]
    list_display = ['name','address','year']

class GameAdmin(admin.ModelAdmin):
    model = Game
    list_filter = ['season', 'host', 'guest']
    list_display = ['season','host','guest','start_time', 'address']

class RefereeAdmin(admin.ModelAdmin):
    model = Season
    list_display = ['name', 'city']
    

admin.site.register(Season, SeasonAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Referee, RefereeAdmin)
