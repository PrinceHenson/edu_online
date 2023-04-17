from django.contrib import admin

from apps.operations.models import CourseComment, UserCourse, UserFavorite,\
    UserMessage


@admin.register(CourseComment)
class CourseCommentAdmin(admin.ModelAdmin):
    list_display = ['course', 'user']
    list_filter = ['course__name', 'user__username']
    search_fields = ['course__name', 'user__username']


@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['user', 'course']
    list_filter = ['user__username', 'course__name']
    search_fields = ['user__username', 'course__name']


@admin.register(UserFavorite)
class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'fav_id', 'fav_type']
    list_filter = ['user__username', 'fav_id', 'fav_type']
    search_fields = ['user__username', 'fav_id', 'fav_type']


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_read', 'message']
    list_filter = ['user__username', 'is_read']
    search_fields = ['user__username', 'is_read']
