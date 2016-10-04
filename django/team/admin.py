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

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from models import UserProfile

class UserProfileInline(admin.StackedInline):
    """"
    Define an inline admin descriptor for UserProfile model 
    which acts a bit like a singleton
    """
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userProfile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)