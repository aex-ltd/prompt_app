from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

from .models import CustomUser 

# customuser admin 
class CustomUserAdmin(UserAdmin):

    model = CustomUser

    list_display = ['email', 'is_active', 'is_staff', 'is_superuser', 'last_login']
    list_display_links = ['email']
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'last_login']
    fieldsets = [
        ('Basic Info', {'fields': ('email','passowrd')}),
        ('Permissions', {'fields':('is_active', 'is_staff','is_superuser', 'groups', 'permissions')}),
        ('Dates', {'fields': ('last_login',)})
    ]
    ordering = ('email',)
    search_fields = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
    
