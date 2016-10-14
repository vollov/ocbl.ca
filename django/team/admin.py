from django.contrib import admin

from models import Team, TeamHistory
from datetime import datetime


class TeamAdmin(admin.ModelAdmin):
    def is_archived(self, team, year):
        mun_of_match = TeamHistory.objects.filter(team=team, year=year).count()
        return mun_of_match > 0
    
    def archive(self, request, queryset):
        rows_updated = 0
        for team in queryset:
            year = datetime.now().year

            if not self.is_archived(team, year):
                teamHistory = TeamHistory(team=team, year=year, name=team.name, city=team.city)
                teamHistory.save()
                rows_updated += 1
            else:
                print 'team name={0}, year={1} already enrolled.'.format(team, year)
        
        if rows_updated == 1:
            message_bit = "1 team was"
        else:
            message_bit = "%s teams were" % rows_updated
        self.message_user(request, "%s successfully enrolled." % message_bit)
    
    archive.short_description = "Archive team"
    
    def activate(self, request, queryset):
        rows_updated = queryset.update(active=True)
        
        if rows_updated == 1:
            message_bit = "1 team was"
        else:
            message_bit = "%s teams were" % rows_updated
        self.message_user(request, "%s successfully activated." % message_bit)
    
    activate.short_description = "Activate Team"
    
    #deactivate cars
    def deactivate(self, request, queryset):
        rows_updated = queryset.update(active=False)
        
        if rows_updated == 1:
            message_bit = "1 team was"
        else:
            message_bit = "%s teams were" % rows_updated
        self.message_user(request, "%s successfully deactivated." % message_bit)
    
    deactivate.short_description = "Deactivate Team"
    
    actions = [archive, activate, deactivate]
    
    list_display = ['name','city','created','active']
    list_filter = ['city']
    
class TeamHistoryAdmin(admin.ModelAdmin):
    list_display = ['name','year']
    list_filter = ['year']

admin.site.register(Team, TeamAdmin)
admin.site.register(TeamHistory, TeamHistoryAdmin)

from team.models import Player
class PlayerAdmin(admin.ModelAdmin):
    model = Player
    
#     def is_captain(self, obj):
#         return obj.user_profile.user.groups.filter(name='captain').exists()
    
    list_display = ['user_profile','team','active', 'number']

admin.site.register(Player, PlayerAdmin)