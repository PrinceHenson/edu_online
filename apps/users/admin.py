from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'gender', 'is_superuser', 'is_staff',
                    'is_active']
    list_filter = ['username', 'gender', 'is_superuser', 'is_staff',
                   'is_active']
    search_fields = ['username', 'gender', 'is_superuser', 'is_staff',
                     'is_active']


admin.site.register(UserProfile, UserAdmin)
