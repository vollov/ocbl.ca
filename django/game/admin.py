from django.contrib import admin

from game.models import Season, Game, Referee, Recorder, Timer, PlayerGameScore

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
    
class RecorderAdmin(admin.ModelAdmin):
    model = Recorder
    list_display = ['name', 'city']
    
class TimerAdmin(admin.ModelAdmin):
    model = Timer
    list_display = ['name', 'city']

admin.site.register(Season, SeasonAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Referee, RefereeAdmin)
admin.site.register(Recorder, RecorderAdmin)
admin.site.register(Timer, TimerAdmin)

class PlayerGameScoreAdmin(admin.ModelAdmin):
    def total_points(self, obj):
        return obj.total_points()
    
    model = PlayerGameScore
    list_display = ['player', 'starters', 'personal_foul', 'free_throw', 'field_goal', 'three_point', 'total_points']
    list_filter = ['game',]
    
admin.site.register(PlayerGameScore, PlayerGameScoreAdmin)