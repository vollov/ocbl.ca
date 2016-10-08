from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userProfile'

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    list_display = ['username', 'first_name','email','date_joined','is_active','is_staff']
    
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
